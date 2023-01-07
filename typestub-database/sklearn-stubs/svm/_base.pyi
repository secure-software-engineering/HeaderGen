from ..base import BaseEstimator as BaseEstimator, ClassifierMixin as ClassifierMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning, NotFittedError as NotFittedError
from ..preprocessing import LabelEncoder as LabelEncoder
from ..utils import check_array as check_array, check_random_state as check_random_state, column_or_1d as column_or_1d, compute_class_weight as compute_class_weight
from ..utils.deprecation import deprecated as deprecated
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ..utils.metaestimators import available_if as available_if
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.validation import check_consistent_length as check_consistent_length, check_is_fitted as check_is_fitted
from abc import ABCMeta, abstractmethod
from typing import Any

LIBSVM_IMPL: Any

class BaseLibSVM(BaseEstimator, metaclass=ABCMeta):
    kernel: Any
    degree: Any
    gamma: Any
    coef0: Any
    tol: Any
    C: Any
    nu: Any
    epsilon: Any
    shrinking: Any
    probability: Any
    cache_size: Any
    class_weight: Any
    verbose: Any
    max_iter: Any
    random_state: Any
    @abstractmethod
    def __init__(self, kernel, degree, gamma, coef0, tol, C, nu, epsilon, shrinking, probability, cache_size, class_weight, verbose, max_iter, random_state): ...
    shape_fit_: Any
    dual_coef_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...
    def predict(self, X): ...
    @property
    def coef_(self): ...
    @property
    def n_support_(self): ...

class BaseSVC(ClassifierMixin, BaseLibSVM, metaclass=ABCMeta):
    decision_function_shape: Any
    break_ties: Any
    @abstractmethod
    def __init__(self, kernel, degree, gamma, coef0, tol, C, nu, shrinking, probability, cache_size, class_weight, verbose, max_iter, decision_function_shape, random_state, break_ties): ...
    def decision_function(self, X): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...
    @property
    def probA_(self): ...
    @property
    def probB_(self): ...
