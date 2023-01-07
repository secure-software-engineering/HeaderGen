from ..base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin
from ..exceptions import NotFittedError as NotFittedError
from ..metrics.pairwise import pairwise_kernels as pairwise_kernels
from ..preprocessing import KernelCenterer as KernelCenterer
from ..utils.deprecation import deprecated as deprecated
from ..utils.extmath import svd_flip as svd_flip
from ..utils.validation import check_is_fitted as check_is_fitted
from typing import Any

class KernelPCA(TransformerMixin, BaseEstimator):
    n_components: Any
    kernel: Any
    kernel_params: Any
    gamma: Any
    degree: Any
    coef0: Any
    alpha: Any
    fit_inverse_transform: Any
    eigen_solver: Any
    tol: Any
    max_iter: Any
    iterated_power: Any
    remove_zero_eig: Any
    random_state: Any
    n_jobs: Any
    copy_X: Any
    def __init__(self, n_components: Any | None = ..., *, kernel: str = ..., gamma: Any | None = ..., degree: int = ..., coef0: int = ..., kernel_params: Any | None = ..., alpha: float = ..., fit_inverse_transform: bool = ..., eigen_solver: str = ..., tol: int = ..., max_iter: Any | None = ..., iterated_power: str = ..., remove_zero_eig: bool = ..., random_state: Any | None = ..., copy_X: bool = ..., n_jobs: Any | None = ...) -> None: ...
    @property
    def lambdas_(self): ...
    @property
    def alphas_(self): ...
    X_fit_: Any
    def fit(self, X, y: Any | None = ...): ...
    def fit_transform(self, X, y: Any | None = ..., **params): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
