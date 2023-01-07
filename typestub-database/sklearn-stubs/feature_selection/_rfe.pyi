from ..base import BaseEstimator as BaseEstimator, MetaEstimatorMixin as MetaEstimatorMixin, clone as clone, is_classifier as is_classifier
from ..metrics import check_scoring as check_scoring
from ..model_selection import check_cv as check_cv
from ..utils.deprecation import deprecated as deprecated
from ..utils.fixes import delayed as delayed
from ..utils.metaestimators import if_delegate_has_method as if_delegate_has_method
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import SelectorMixin as SelectorMixin
from typing import Any

class RFE(SelectorMixin, MetaEstimatorMixin, BaseEstimator):
    estimator: Any
    n_features_to_select: Any
    step: Any
    importance_getter: Any
    verbose: Any
    def __init__(self, estimator, *, n_features_to_select: Any | None = ..., step: int = ..., verbose: int = ..., importance_getter: str = ...) -> None: ...
    @property
    def classes_(self): ...
    def fit(self, X, y, **fit_params): ...
    def predict(self, X): ...
    def score(self, X, y, **fit_params): ...
    def decision_function(self, X): ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...

class RFECV(RFE):
    estimator: Any
    step: Any
    importance_getter: Any
    cv: Any
    scoring: Any
    verbose: Any
    n_jobs: Any
    min_features_to_select: Any
    def __init__(self, estimator, *, step: int = ..., min_features_to_select: int = ..., cv: Any | None = ..., scoring: Any | None = ..., verbose: int = ..., n_jobs: Any | None = ..., importance_getter: str = ...) -> None: ...
    support_: Any
    n_features_: Any
    ranking_: Any
    estimator_: Any
    cv_results_: Any
    def fit(self, X, y, groups: Any | None = ...): ...
    @property
    def grid_scores_(self): ...
