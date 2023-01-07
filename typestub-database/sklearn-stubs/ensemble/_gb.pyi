from ..base import BaseEstimator as BaseEstimator, ClassifierMixin as ClassifierMixin, RegressorMixin as RegressorMixin, is_classifier as is_classifier
from ..exceptions import NotFittedError as NotFittedError
from ..model_selection import train_test_split as train_test_split
from ..tree import DecisionTreeRegressor as DecisionTreeRegressor
from ..tree._tree import DOUBLE as DOUBLE, DTYPE as DTYPE
from ..utils import check_array as check_array, check_random_state as check_random_state, column_or_1d as column_or_1d, deprecated as deprecated
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import BaseEnsemble as BaseEnsemble
from ._gradient_boosting import predict_stage as predict_stage, predict_stages as predict_stages
from abc import ABCMeta, abstractmethod
from typing import Any

class VerboseReporter:
    verbose: Any
    def __init__(self, verbose) -> None: ...
    verbose_fmt: Any
    verbose_mod: int
    start_time: Any
    begin_at_stage: Any
    def init(self, est, begin_at_stage: int = ...) -> None: ...
    def update(self, j, est) -> None: ...

class BaseGradientBoosting(BaseEnsemble, metaclass=ABCMeta):
    n_estimators: Any
    learning_rate: Any
    loss: Any
    criterion: Any
    min_samples_split: Any
    min_samples_leaf: Any
    min_weight_fraction_leaf: Any
    subsample: Any
    max_features: Any
    max_depth: Any
    min_impurity_decrease: Any
    ccp_alpha: Any
    init: Any
    random_state: Any
    alpha: Any
    verbose: Any
    max_leaf_nodes: Any
    warm_start: Any
    validation_fraction: Any
    n_iter_no_change: Any
    tol: Any
    @abstractmethod
    def __init__(self, loss, learning_rate, n_estimators, criterion, min_samples_split, min_samples_leaf, min_weight_fraction_leaf, max_depth, min_impurity_decrease, init, subsample, max_features, ccp_alpha, random_state, *, alpha: float = ..., verbose: int = ..., max_leaf_nodes: Any | None = ..., warm_start: bool = ..., validation_fraction: float = ..., n_iter_no_change: Any | None = ..., tol: float = ...): ...
    estimators_: Any
    train_score_: Any
    oob_improvement_: Any
    n_estimators_: Any
    def fit(self, X, y, sample_weight: Any | None = ..., monitor: Any | None = ...): ...
    @property
    def feature_importances_(self): ...
    def apply(self, X): ...
    @property
    def n_features_(self): ...

class GradientBoostingClassifier(ClassifierMixin, BaseGradientBoosting):
    def __init__(self, *, loss: str = ..., learning_rate: float = ..., n_estimators: int = ..., subsample: float = ..., criterion: str = ..., min_samples_split: int = ..., min_samples_leaf: int = ..., min_weight_fraction_leaf: float = ..., max_depth: int = ..., min_impurity_decrease: float = ..., init: Any | None = ..., random_state: Any | None = ..., max_features: Any | None = ..., verbose: int = ..., max_leaf_nodes: Any | None = ..., warm_start: bool = ..., validation_fraction: float = ..., n_iter_no_change: Any | None = ..., tol: float = ..., ccp_alpha: float = ...) -> None: ...
    def decision_function(self, X): ...
    def staged_decision_function(self, X) -> None: ...
    def predict(self, X): ...
    def staged_predict(self, X) -> None: ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...
    def staged_predict_proba(self, X) -> None: ...

class GradientBoostingRegressor(RegressorMixin, BaseGradientBoosting):
    def __init__(self, *, loss: str = ..., learning_rate: float = ..., n_estimators: int = ..., subsample: float = ..., criterion: str = ..., min_samples_split: int = ..., min_samples_leaf: int = ..., min_weight_fraction_leaf: float = ..., max_depth: int = ..., min_impurity_decrease: float = ..., init: Any | None = ..., random_state: Any | None = ..., max_features: Any | None = ..., alpha: float = ..., verbose: int = ..., max_leaf_nodes: Any | None = ..., warm_start: bool = ..., validation_fraction: float = ..., n_iter_no_change: Any | None = ..., tol: float = ..., ccp_alpha: float = ...) -> None: ...
    def predict(self, X): ...
    def staged_predict(self, X) -> None: ...
    def apply(self, X): ...
    @property
    def n_classes_(self): ...
