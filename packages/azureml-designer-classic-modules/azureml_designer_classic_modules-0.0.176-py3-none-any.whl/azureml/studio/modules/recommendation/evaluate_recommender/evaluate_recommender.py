from azureml.studio.core.logger import TimeProfile
from azureml.studio.modulehost.module_reflector import BaseModule, module_entry
from azureml.studio.modulehost.attributes import ModuleMeta, DataTableOutputPort, DataTableInputPort
from azureml.studio.internal.attributes.release_state import ReleaseState
from azureml.studio.common.datatable.data_table import DataTable
from azureml.studio.modules.recommendation.evaluate_recommender.recommendation_task import build_recommendation_task
from azureml.studio.modules.ml.common.constants import ScoreColumnConstants
from azureml.studio.common.error import ErrorMapping, InvalidDatasetError
from azureml.studio.modules.ml.common.metrics_logger import common_evaluate_model_metrics_logger


class EvaluateRecommenderModule(BaseModule):
    @staticmethod
    @module_entry(ModuleMeta(
        name="Evaluate Recommender",
        description="Evaluate a recommendation model.",
        category="Recommendation",
        version="1.0",
        owner="Microsoft Corporation",
        family_id="{9C4D0CB5-213E-4785-9CC8-D29CE467B9C8}",
        release_state=ReleaseState.Release,
        is_deterministic=True,
    ))
    def run(
            test_data: DataTableInputPort(
                name="Test dataset",
                friendly_name="Test dataset",
                description="Test dataset",
            ),
            scored_data: DataTableInputPort(
                name="Scored dataset",
                friendly_name="Scored dataset",
                description="Scored dataset",
            )
    ) -> (
            DataTableOutputPort(
                name="Metric",
                friendly_name="Metric",
                description="A table of evaluation metrics",
            ),
    ):
        input_values = locals()
        output_values = EvaluateRecommenderModule.evaluate_recommender(**input_values)
        return output_values

    @classmethod
    def evaluate_recommender(cls, scored_data: DataTable, test_data: DataTable = None):
        with TimeProfile("Deduce recommendation task"):
            task = build_recommendation_task(scored_data)

            # when task is None, the scored_data is not generated by score recommender modules,
            # detect if is generated by 'Score Model' module. Because the Evaluate Recommender input
            # port order is 'Test dataset' first, so we should detect both scored data and test data,
            # just in case that input dataset are reversed.
            if task is None:
                invalid_dataset_reason = "because it is not generated by recommender scoring modules"
                invalid_dataset_name = scored_data.name

                if cls.is_evaluate_model_scored_data_input(dt=scored_data) or \
                        cls.is_evaluate_model_scored_data_input(dt=test_data):
                    invalid_dataset_reason = 'it\'s not a valid recommendation result. ' \
                                             'Please use "Evaluate Model" module instead'

                if test_data and build_recommendation_task(test_data):
                    # detect if scored dataset and test dataset are misplaced. Because test dataset columns format
                    # is similar to regression scored dataset, so regression task is excluded.
                    invalid_dataset_reason = f'{scored_data.name} and {test_data.name} are misplaced'

                ErrorMapping.throw(InvalidDatasetError(dataset1=invalid_dataset_name, reason=invalid_dataset_reason))

        metrics_dt = task.evaluate(scored_data=scored_data, test_data=test_data)
        # build metrics tab
        common_evaluate_model_metrics_logger.log_metrics(data=metrics_dt.data_frame)
        return metrics_dt,

    @staticmethod
    def is_evaluate_model_scored_data_input(dt: DataTable = None):
        if dt is None:
            return False

        checked_scored_label_types = [ScoreColumnConstants.BinaryClassScoredLabelType,
                                      ScoreColumnConstants.MultiClassScoredLabelType,
                                      ScoreColumnConstants.RegressionScoredLabelType,
                                      ScoreColumnConstants.ClusterScoredLabelType,
                                      ScoreColumnConstants.AnomalyDetectionScoredLabelType]
        # if any label type of checked_scored_label_types in score_columns, it is a input
        # for evaluate model module
        score_columns = dt.meta_data.score_column_names
        is_evaluate_model_input = any(label_type in score_columns for label_type in checked_scored_label_types)

        # check if dt is a scored data generated by legacy score model
        if not is_evaluate_model_input:
            extended_properties = dt.meta_data.extended_properties
            is_evaluate_model_input = (
                    extended_properties is not None and 'is_scored_data' in extended_properties
                    and 'learner_type' in extended_properties)
        return is_evaluate_model_input
