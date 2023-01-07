from ..base import BaseEstimator as BaseEstimator
from ..utils.sparsefuncs import mean_variance_axis as mean_variance_axis, min_max_axis as min_max_axis
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import SelectorMixin as SelectorMixin
from typing import Any

class VarianceThreshold(SelectorMixin, BaseEstimator):
    threshold: Any
    def __init__(self, threshold: float = ...) -> None: ...
    variances_: Any
    def fit(self, X, y: Any | None = ...): ...
