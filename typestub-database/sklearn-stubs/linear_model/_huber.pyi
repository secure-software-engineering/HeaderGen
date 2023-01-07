from ..base import BaseEstimator as BaseEstimator, RegressorMixin as RegressorMixin
from ..utils import axis0_safe_slice as axis0_safe_slice
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ._base import LinearModel as LinearModel
from typing import Any

class HuberRegressor(LinearModel, RegressorMixin, BaseEstimator):
    epsilon: Any
    max_iter: Any
    alpha: Any
    warm_start: Any
    fit_intercept: Any
    tol: Any
    def __init__(self, *, epsilon: float = ..., max_iter: int = ..., alpha: float = ..., warm_start: bool = ..., fit_intercept: bool = ..., tol: float = ...) -> None: ...
    n_iter_: Any
    scale_: Any
    intercept_: Any
    coef_: Any
    outliers_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...
