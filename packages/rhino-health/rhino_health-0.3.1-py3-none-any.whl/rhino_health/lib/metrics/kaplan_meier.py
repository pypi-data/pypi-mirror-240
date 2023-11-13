from rhino_health.lib.metrics.base_metric import (
    AggregatableMetric,
    BaseMetric,
    KaplanMeierMetricResponse,
)
from rhino_health.lib.metrics.filter_variable import FilterVariableTypeOrColumnName


class KaplanMeier(AggregatableMetric):
    """
    Returns the k-percentile of entries for a specified VARIABLE
    """

    time_variable: FilterVariableTypeOrColumnName
    event_variable: FilterVariableTypeOrColumnName

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def metric_name(cls):
        return "kaplan_meier"

    @property
    def metric_response(self):
        return KaplanMeierMetricResponse

    @property
    def supports_custom_aggregation(self):
        return False
