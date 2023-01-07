from statsmodels.base.elastic_net import RegularizedResults as RegularizedResults
from statsmodels.base.model import LikelihoodModelResults as LikelihoodModelResults
from statsmodels.regression.linear_model import OLS as OLS
from typing import Any

class DistributedModel:
    __doc__: str
    partitions: Any
    model_class: Any
    init_kwds: Any
    estimation_method: Any
    estimation_kwds: Any
    join_method: Any
    join_kwds: Any
    results_class: Any
    results_kwds: Any
    def __init__(self, partitions, model_class: Any | None = ..., init_kwds: Any | None = ..., estimation_method: Any | None = ..., estimation_kwds: Any | None = ..., join_method: Any | None = ..., join_kwds: Any | None = ..., results_class: Any | None = ..., results_kwds: Any | None = ...) -> None: ...
    def fit(self, data_generator, fit_kwds: Any | None = ..., parallel_method: str = ..., parallel_backend: Any | None = ..., init_kwds_generator: Any | None = ...): ...
    def fit_sequential(self, data_generator, fit_kwds, init_kwds_generator: Any | None = ...): ...
    def fit_joblib(self, data_generator, fit_kwds, parallel_backend, init_kwds_generator: Any | None = ...): ...

class DistributedResults(LikelihoodModelResults):
    def __init__(self, model, params) -> None: ...
    def predict(self, exog, *args, **kwargs): ...
