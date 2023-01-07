import abc
from ..base import MultiOutputMixin as MultiOutputMixin, RegressorMixin as RegressorMixin
from ..model_selection import check_cv as check_cv
from ..utils import check_array as check_array
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ..utils.fixes import delayed as delayed
from ..utils.validation import check_consistent_length as check_consistent_length, check_is_fitted as check_is_fitted, check_random_state as check_random_state, column_or_1d as column_or_1d
from ._base import LinearModel as LinearModel
from abc import ABC, abstractmethod
from typing import Any

def lasso_path(X, y, *, eps: float = ..., n_alphas: int = ..., alphas: Any | None = ..., precompute: str = ..., Xy: Any | None = ..., copy_X: bool = ..., coef_init: Any | None = ..., verbose: bool = ..., return_n_iter: bool = ..., positive: bool = ..., **params): ...
def enet_path(X, y, *, l1_ratio: float = ..., eps: float = ..., n_alphas: int = ..., alphas: Any | None = ..., precompute: str = ..., Xy: Any | None = ..., copy_X: bool = ..., coef_init: Any | None = ..., verbose: bool = ..., return_n_iter: bool = ..., positive: bool = ..., check_input: bool = ..., **params): ...

class ElasticNet(MultiOutputMixin, RegressorMixin, LinearModel):
    path: Any
    alpha: Any
    l1_ratio: Any
    fit_intercept: Any
    normalize: Any
    precompute: Any
    max_iter: Any
    copy_X: Any
    tol: Any
    warm_start: Any
    positive: Any
    random_state: Any
    selection: Any
    def __init__(self, alpha: float = ..., *, l1_ratio: float = ..., fit_intercept: bool = ..., normalize: str = ..., precompute: bool = ..., max_iter: int = ..., copy_X: bool = ..., tol: float = ..., warm_start: bool = ..., positive: bool = ..., random_state: Any | None = ..., selection: str = ...) -> None: ...
    n_iter_: Any
    coef_: Any
    dual_gap_: Any
    def fit(self, X, y, sample_weight: Any | None = ..., check_input: bool = ...): ...
    @property
    def sparse_coef_(self): ...

class Lasso(ElasticNet):
    path: Any
    def __init__(self, alpha: float = ..., *, fit_intercept: bool = ..., normalize: str = ..., precompute: bool = ..., copy_X: bool = ..., max_iter: int = ..., tol: float = ..., warm_start: bool = ..., positive: bool = ..., random_state: Any | None = ..., selection: str = ...) -> None: ...

class LinearModelCV(MultiOutputMixin, LinearModel, ABC, metaclass=abc.ABCMeta):
    eps: Any
    n_alphas: Any
    alphas: Any
    fit_intercept: Any
    normalize: Any
    precompute: Any
    max_iter: Any
    tol: Any
    copy_X: Any
    cv: Any
    verbose: Any
    n_jobs: Any
    positive: Any
    random_state: Any
    selection: Any
    @abstractmethod
    def __init__(self, eps: float = ..., n_alphas: int = ..., alphas: Any | None = ..., fit_intercept: bool = ..., normalize: str = ..., precompute: str = ..., max_iter: int = ..., tol: float = ..., copy_X: bool = ..., cv: Any | None = ..., verbose: bool = ..., n_jobs: Any | None = ..., positive: bool = ..., random_state: Any | None = ..., selection: str = ...): ...
    @staticmethod
    @abstractmethod
    def path(X, y, **kwargs): ...
    mse_path_: Any
    l1_ratio_: Any
    alpha_: Any
    alphas_: Any
    coef_: Any
    intercept_: Any
    dual_gap_: Any
    n_iter_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...

class LassoCV(RegressorMixin, LinearModelCV):
    path: Any
    def __init__(self, *, eps: float = ..., n_alphas: int = ..., alphas: Any | None = ..., fit_intercept: bool = ..., normalize: str = ..., precompute: str = ..., max_iter: int = ..., tol: float = ..., copy_X: bool = ..., cv: Any | None = ..., verbose: bool = ..., n_jobs: Any | None = ..., positive: bool = ..., random_state: Any | None = ..., selection: str = ...) -> None: ...

class ElasticNetCV(RegressorMixin, LinearModelCV):
    path: Any
    l1_ratio: Any
    eps: Any
    n_alphas: Any
    alphas: Any
    fit_intercept: Any
    normalize: Any
    precompute: Any
    max_iter: Any
    tol: Any
    cv: Any
    copy_X: Any
    verbose: Any
    n_jobs: Any
    positive: Any
    random_state: Any
    selection: Any
    def __init__(self, *, l1_ratio: float = ..., eps: float = ..., n_alphas: int = ..., alphas: Any | None = ..., fit_intercept: bool = ..., normalize: str = ..., precompute: str = ..., max_iter: int = ..., tol: float = ..., cv: Any | None = ..., copy_X: bool = ..., verbose: int = ..., n_jobs: Any | None = ..., positive: bool = ..., random_state: Any | None = ..., selection: str = ...) -> None: ...

class MultiTaskElasticNet(Lasso):
    l1_ratio: Any
    alpha: Any
    fit_intercept: Any
    normalize: Any
    max_iter: Any
    copy_X: Any
    tol: Any
    warm_start: Any
    random_state: Any
    selection: Any
    def __init__(self, alpha: float = ..., *, l1_ratio: float = ..., fit_intercept: bool = ..., normalize: str = ..., copy_X: bool = ..., max_iter: int = ..., tol: float = ..., warm_start: bool = ..., random_state: Any | None = ..., selection: str = ...) -> None: ...
    coef_: Any
    def fit(self, X, y): ...

class MultiTaskLasso(MultiTaskElasticNet):
    alpha: Any
    fit_intercept: Any
    normalize: Any
    max_iter: Any
    copy_X: Any
    tol: Any
    warm_start: Any
    l1_ratio: float
    random_state: Any
    selection: Any
    def __init__(self, alpha: float = ..., *, fit_intercept: bool = ..., normalize: str = ..., copy_X: bool = ..., max_iter: int = ..., tol: float = ..., warm_start: bool = ..., random_state: Any | None = ..., selection: str = ...) -> None: ...

class MultiTaskElasticNetCV(RegressorMixin, LinearModelCV):
    path: Any
    l1_ratio: Any
    eps: Any
    n_alphas: Any
    alphas: Any
    fit_intercept: Any
    normalize: Any
    max_iter: Any
    tol: Any
    cv: Any
    copy_X: Any
    verbose: Any
    n_jobs: Any
    random_state: Any
    selection: Any
    def __init__(self, *, l1_ratio: float = ..., eps: float = ..., n_alphas: int = ..., alphas: Any | None = ..., fit_intercept: bool = ..., normalize: str = ..., max_iter: int = ..., tol: float = ..., cv: Any | None = ..., copy_X: bool = ..., verbose: int = ..., n_jobs: Any | None = ..., random_state: Any | None = ..., selection: str = ...) -> None: ...
    def fit(self, X, y): ...

class MultiTaskLassoCV(RegressorMixin, LinearModelCV):
    path: Any
    def __init__(self, *, eps: float = ..., n_alphas: int = ..., alphas: Any | None = ..., fit_intercept: bool = ..., normalize: str = ..., max_iter: int = ..., tol: float = ..., copy_X: bool = ..., cv: Any | None = ..., verbose: bool = ..., n_jobs: Any | None = ..., random_state: Any | None = ..., selection: str = ...) -> None: ...
    def fit(self, X, y): ...
