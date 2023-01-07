from .base import BaseEstimator as BaseEstimator, MultiOutputMixin as MultiOutputMixin, RegressorMixin as RegressorMixin
from .metrics.pairwise import pairwise_kernels as pairwise_kernels
from .utils.deprecation import deprecated as deprecated
from .utils.validation import check_is_fitted as check_is_fitted
from typing import Any

class KernelRidge(MultiOutputMixin, RegressorMixin, BaseEstimator):
    alpha: Any
    kernel: Any
    gamma: Any
    degree: Any
    coef0: Any
    kernel_params: Any
    def __init__(self, alpha: int = ..., *, kernel: str = ..., gamma: Any | None = ..., degree: int = ..., coef0: int = ..., kernel_params: Any | None = ...) -> None: ...
    dual_coef_: Any
    X_fit_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...
    def predict(self, X): ...
