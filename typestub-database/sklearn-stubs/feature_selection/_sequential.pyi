from ..base import BaseEstimator as BaseEstimator, MetaEstimatorMixin as MetaEstimatorMixin, clone as clone
from ..model_selection import cross_val_score as cross_val_score
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import SelectorMixin as SelectorMixin
from typing import Any

class SequentialFeatureSelector(SelectorMixin, MetaEstimatorMixin, BaseEstimator):
    estimator: Any
    n_features_to_select: Any
    direction: Any
    scoring: Any
    cv: Any
    n_jobs: Any
    def __init__(self, estimator, *, n_features_to_select: Any | None = ..., direction: str = ..., scoring: Any | None = ..., cv: int = ..., n_jobs: Any | None = ...) -> None: ...
    n_features_to_select_: Any
    support_: Any
    def fit(self, X, y: Any | None = ...): ...
