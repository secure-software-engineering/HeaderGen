from ..base import BaseEstimator as BaseEstimator, RegressorMixin as RegressorMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils.fixes import parse_version as parse_version, sp_version as sp_version
from ._base import LinearModel as LinearModel
from typing import Any

class QuantileRegressor(LinearModel, RegressorMixin, BaseEstimator):
    quantile: Any
    alpha: Any
    fit_intercept: Any
    solver: Any
    solver_options: Any
    def __init__(self, *, quantile: float = ..., alpha: float = ..., fit_intercept: bool = ..., solver: str = ..., solver_options: Any | None = ...) -> None: ...
    n_iter_: Any
    coef_: Any
    intercept_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...
