from ..base import BaseEstimator as BaseEstimator, ClassifierMixin as ClassifierMixin, RegressorMixin as RegressorMixin, is_classifier as is_classifier
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..model_selection import train_test_split as train_test_split
from ..preprocessing import LabelBinarizer as LabelBinarizer
from ..utils import check_random_state as check_random_state, column_or_1d as column_or_1d, gen_batches as gen_batches, shuffle as shuffle
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ..utils.metaestimators import available_if as available_if
from ..utils.multiclass import type_of_target as type_of_target, unique_labels as unique_labels
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import ACTIVATIONS as ACTIVATIONS, DERIVATIVES as DERIVATIVES, LOSS_FUNCTIONS as LOSS_FUNCTIONS
from ._stochastic_optimizers import AdamOptimizer as AdamOptimizer, SGDOptimizer as SGDOptimizer
from abc import ABCMeta, abstractmethod
from typing import Any

class BaseMultilayerPerceptron(BaseEstimator, metaclass=ABCMeta):
    activation: Any
    solver: Any
    alpha: Any
    batch_size: Any
    learning_rate: Any
    learning_rate_init: Any
    power_t: Any
    max_iter: Any
    loss: Any
    hidden_layer_sizes: Any
    shuffle: Any
    random_state: Any
    tol: Any
    verbose: Any
    warm_start: Any
    momentum: Any
    nesterovs_momentum: Any
    early_stopping: Any
    validation_fraction: Any
    beta_1: Any
    beta_2: Any
    epsilon: Any
    n_iter_no_change: Any
    max_fun: Any
    @abstractmethod
    def __init__(self, hidden_layer_sizes, activation, solver, alpha, batch_size, learning_rate, learning_rate_init, power_t, max_iter, loss, shuffle, random_state, tol, verbose, warm_start, momentum, nesterovs_momentum, early_stopping, validation_fraction, beta_1, beta_2, epsilon, n_iter_no_change, max_fun): ...
    def fit(self, X, y): ...
    def partial_fit(self, X, y): ...

class MLPClassifier(ClassifierMixin, BaseMultilayerPerceptron):
    def __init__(self, hidden_layer_sizes=..., activation: str = ..., *, solver: str = ..., alpha: float = ..., batch_size: str = ..., learning_rate: str = ..., learning_rate_init: float = ..., power_t: float = ..., max_iter: int = ..., shuffle: bool = ..., random_state: Any | None = ..., tol: float = ..., verbose: bool = ..., warm_start: bool = ..., momentum: float = ..., nesterovs_momentum: bool = ..., early_stopping: bool = ..., validation_fraction: float = ..., beta_1: float = ..., beta_2: float = ..., epsilon: float = ..., n_iter_no_change: int = ..., max_fun: int = ...) -> None: ...
    def predict(self, X): ...
    def partial_fit(self, X, y, classes: Any | None = ...): ...
    def predict_log_proba(self, X): ...
    def predict_proba(self, X): ...

class MLPRegressor(RegressorMixin, BaseMultilayerPerceptron):
    def __init__(self, hidden_layer_sizes=..., activation: str = ..., *, solver: str = ..., alpha: float = ..., batch_size: str = ..., learning_rate: str = ..., learning_rate_init: float = ..., power_t: float = ..., max_iter: int = ..., shuffle: bool = ..., random_state: Any | None = ..., tol: float = ..., verbose: bool = ..., warm_start: bool = ..., momentum: float = ..., nesterovs_momentum: bool = ..., early_stopping: bool = ..., validation_fraction: float = ..., beta_1: float = ..., beta_2: float = ..., epsilon: float = ..., n_iter_no_change: int = ..., max_fun: int = ...) -> None: ...
    def predict(self, X): ...
