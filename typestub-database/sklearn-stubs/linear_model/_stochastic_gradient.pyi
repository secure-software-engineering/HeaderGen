import abc
from ..base import BaseEstimator as BaseEstimator, OutlierMixin as OutlierMixin, RegressorMixin as RegressorMixin, clone as clone, is_classifier as is_classifier
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..model_selection import ShuffleSplit as ShuffleSplit, StratifiedShuffleSplit as StratifiedShuffleSplit
from ..utils import check_random_state as check_random_state, compute_class_weight as compute_class_weight
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ..utils.fixes import delayed as delayed
from ..utils.metaestimators import available_if as available_if
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import LinearClassifierMixin as LinearClassifierMixin, SparseCoefMixin as SparseCoefMixin, make_dataset as make_dataset
from ._sgd_fast import EpsilonInsensitive as EpsilonInsensitive, Hinge as Hinge, Huber as Huber, Log as Log, ModifiedHuber as ModifiedHuber, SquaredEpsilonInsensitive as SquaredEpsilonInsensitive, SquaredHinge as SquaredHinge, SquaredLoss as SquaredLoss
from abc import ABCMeta, abstractmethod
from typing import Any

LEARNING_RATE_TYPES: Any
PENALTY_TYPES: Any
DEFAULT_EPSILON: float
MAX_INT: Any

class _ValidationScoreCallback:
    estimator: Any
    X_val: Any
    y_val: Any
    sample_weight_val: Any
    def __init__(self, estimator, X_val, y_val, sample_weight_val, classes: Any | None = ...) -> None: ...
    def __call__(self, coef, intercept): ...

class BaseSGD(SparseCoefMixin, BaseEstimator, metaclass=ABCMeta):
    loss: Any
    penalty: Any
    learning_rate: Any
    epsilon: Any
    alpha: Any
    C: Any
    l1_ratio: Any
    fit_intercept: Any
    shuffle: Any
    random_state: Any
    verbose: Any
    eta0: Any
    power_t: Any
    early_stopping: Any
    validation_fraction: Any
    n_iter_no_change: Any
    warm_start: Any
    average: Any
    max_iter: Any
    tol: Any
    def __init__(self, loss, *, penalty: str = ..., alpha: float = ..., C: float = ..., l1_ratio: float = ..., fit_intercept: bool = ..., max_iter: int = ..., tol: float = ..., shuffle: bool = ..., verbose: int = ..., epsilon: float = ..., random_state: Any | None = ..., learning_rate: str = ..., eta0: float = ..., power_t: float = ..., early_stopping: bool = ..., validation_fraction: float = ..., n_iter_no_change: int = ..., warm_start: bool = ..., average: bool = ...) -> None: ...
    @abstractmethod
    def fit(self, X, y): ...

def fit_binary(est, i, X, y, alpha, C, learning_rate, max_iter, pos_weight, neg_weight, sample_weight, validation_mask: Any | None = ..., random_state: Any | None = ...): ...

class BaseSGDClassifier(LinearClassifierMixin, BaseSGD, metaclass=ABCMeta):
    loss_functions: Any
    class_weight: Any
    n_jobs: Any
    @abstractmethod
    def __init__(self, loss: str = ..., *, penalty: str = ..., alpha: float = ..., l1_ratio: float = ..., fit_intercept: bool = ..., max_iter: int = ..., tol: float = ..., shuffle: bool = ..., verbose: int = ..., epsilon=..., n_jobs: Any | None = ..., random_state: Any | None = ..., learning_rate: str = ..., eta0: float = ..., power_t: float = ..., early_stopping: bool = ..., validation_fraction: float = ..., n_iter_no_change: int = ..., class_weight: Any | None = ..., warm_start: bool = ..., average: bool = ...): ...
    def partial_fit(self, X, y, classes: Any | None = ..., sample_weight: Any | None = ...): ...
    def fit(self, X, y, coef_init: Any | None = ..., intercept_init: Any | None = ..., sample_weight: Any | None = ...): ...

class SGDClassifier(BaseSGDClassifier):
    def __init__(self, loss: str = ..., *, penalty: str = ..., alpha: float = ..., l1_ratio: float = ..., fit_intercept: bool = ..., max_iter: int = ..., tol: float = ..., shuffle: bool = ..., verbose: int = ..., epsilon=..., n_jobs: Any | None = ..., random_state: Any | None = ..., learning_rate: str = ..., eta0: float = ..., power_t: float = ..., early_stopping: bool = ..., validation_fraction: float = ..., n_iter_no_change: int = ..., class_weight: Any | None = ..., warm_start: bool = ..., average: bool = ...) -> None: ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...

class BaseSGDRegressor(RegressorMixin, BaseSGD, metaclass=abc.ABCMeta):
    loss_functions: Any
    @abstractmethod
    def __init__(self, loss: str = ..., *, penalty: str = ..., alpha: float = ..., l1_ratio: float = ..., fit_intercept: bool = ..., max_iter: int = ..., tol: float = ..., shuffle: bool = ..., verbose: int = ..., epsilon=..., random_state: Any | None = ..., learning_rate: str = ..., eta0: float = ..., power_t: float = ..., early_stopping: bool = ..., validation_fraction: float = ..., n_iter_no_change: int = ..., warm_start: bool = ..., average: bool = ...): ...
    def partial_fit(self, X, y, sample_weight: Any | None = ...): ...
    def fit(self, X, y, coef_init: Any | None = ..., intercept_init: Any | None = ..., sample_weight: Any | None = ...): ...
    def predict(self, X): ...

class SGDRegressor(BaseSGDRegressor):
    def __init__(self, loss: str = ..., *, penalty: str = ..., alpha: float = ..., l1_ratio: float = ..., fit_intercept: bool = ..., max_iter: int = ..., tol: float = ..., shuffle: bool = ..., verbose: int = ..., epsilon=..., random_state: Any | None = ..., learning_rate: str = ..., eta0: float = ..., power_t: float = ..., early_stopping: bool = ..., validation_fraction: float = ..., n_iter_no_change: int = ..., warm_start: bool = ..., average: bool = ...) -> None: ...

class SGDOneClassSVM(BaseSGD, OutlierMixin):
    loss_functions: Any
    nu: Any
    def __init__(self, nu: float = ..., fit_intercept: bool = ..., max_iter: int = ..., tol: float = ..., shuffle: bool = ..., verbose: int = ..., random_state: Any | None = ..., learning_rate: str = ..., eta0: float = ..., power_t: float = ..., warm_start: bool = ..., average: bool = ...) -> None: ...
    def partial_fit(self, X, y: Any | None = ..., sample_weight: Any | None = ...): ...
    def fit(self, X, y: Any | None = ..., coef_init: Any | None = ..., offset_init: Any | None = ..., sample_weight: Any | None = ...): ...
    def decision_function(self, X): ...
    def score_samples(self, X): ...
    def predict(self, X): ...
