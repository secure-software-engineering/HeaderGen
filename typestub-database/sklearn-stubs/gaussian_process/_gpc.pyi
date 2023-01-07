from ..base import BaseEstimator as BaseEstimator, ClassifierMixin as ClassifierMixin, clone as clone
from ..multiclass import OneVsOneClassifier as OneVsOneClassifier, OneVsRestClassifier as OneVsRestClassifier
from ..preprocessing import LabelEncoder as LabelEncoder
from ..utils import check_random_state as check_random_state
from ..utils.validation import check_is_fitted as check_is_fitted
from .kernels import CompoundKernel as CompoundKernel, RBF as RBF
from typing import Any

LAMBDAS: Any
COEFS: Any

class _BinaryGaussianProcessClassifierLaplace(BaseEstimator):
    kernel: Any
    optimizer: Any
    n_restarts_optimizer: Any
    max_iter_predict: Any
    warm_start: Any
    copy_X_train: Any
    random_state: Any
    def __init__(self, kernel: Any | None = ..., *, optimizer: str = ..., n_restarts_optimizer: int = ..., max_iter_predict: int = ..., warm_start: bool = ..., copy_X_train: bool = ..., random_state: Any | None = ...) -> None: ...
    kernel_: Any
    rng: Any
    X_train_: Any
    y_train_: Any
    classes_: Any
    log_marginal_likelihood_value_: Any
    def fit(self, X, y): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def log_marginal_likelihood(self, theta: Any | None = ..., eval_gradient: bool = ..., clone_kernel: bool = ...): ...

class GaussianProcessClassifier(ClassifierMixin, BaseEstimator):
    kernel: Any
    optimizer: Any
    n_restarts_optimizer: Any
    max_iter_predict: Any
    warm_start: Any
    copy_X_train: Any
    random_state: Any
    multi_class: Any
    n_jobs: Any
    def __init__(self, kernel: Any | None = ..., *, optimizer: str = ..., n_restarts_optimizer: int = ..., max_iter_predict: int = ..., warm_start: bool = ..., copy_X_train: bool = ..., random_state: Any | None = ..., multi_class: str = ..., n_jobs: Any | None = ...) -> None: ...
    base_estimator_: Any
    classes_: Any
    n_classes_: Any
    log_marginal_likelihood_value_: Any
    def fit(self, X, y): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    @property
    def kernel_(self): ...
    def log_marginal_likelihood(self, theta: Any | None = ..., eval_gradient: bool = ..., clone_kernel: bool = ...): ...
