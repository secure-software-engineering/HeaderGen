from .multivariate_ols import multivariate_stats as multivariate_stats
from statsmodels.base.model import Model as Model
from statsmodels.iolib import summary2 as summary2
from typing import Any

class CanCorr(Model):
    def __init__(self, endog, exog, tolerance: float = ..., missing: str = ..., hasconst: Any | None = ..., **kwargs) -> None: ...
    def corr_test(self): ...

class CanCorrTestResults:
    stats: Any
    stats_mv: Any
    def __init__(self, stats, stats_mv) -> None: ...
    def summary(self): ...
