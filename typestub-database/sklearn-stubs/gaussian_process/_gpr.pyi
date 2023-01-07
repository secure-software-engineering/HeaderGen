from ..base import BaseEstimator as BaseEstimator, MultiOutputMixin as MultiOutputMixin, RegressorMixin as RegressorMixin, clone as clone
from ..utils import check_random_state as check_random_state
from .kernels import RBF as RBF
from typing import Any

GPR_CHOLESKY_LOWER: bool

class GaussianProcessRegressor(MultiOutputMixin, RegressorMixin, BaseEstimator):
    kernel: Any
    alpha: Any
    optimizer: Any
    n_restarts_optimizer: Any
    normalize_y: Any
    copy_X_train: Any
    random_state: Any
    def __init__(self, kernel: Any | None = ..., *, alpha: float = ..., optimizer: str = ..., n_restarts_optimizer: int = ..., normalize_y: bool = ..., copy_X_train: bool = ..., random_state: Any | None = ...) -> None: ...
    kernel_: Any
    X_train_: Any
    y_train_: Any
    log_marginal_likelihood_value_: Any
    L_: Any
    alpha_: Any
    def fit(self, X, y): ...
    def predict(self, X, return_std: bool = ..., return_cov: bool = ...): ...
    def sample_y(self, X, n_samples: int = ..., random_state: int = ...): ...
    def log_marginal_likelihood(self, theta: Any | None = ..., eval_gradient: bool = ..., clone_kernel: bool = ...): ...
