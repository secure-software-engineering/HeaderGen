from .._config import config_context as config_context
from ..base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils import check_array as check_array, check_random_state as check_random_state
from ..utils.extmath import randomized_svd as randomized_svd, safe_sparse_dot as safe_sparse_dot, squared_norm as squared_norm
from ..utils.validation import check_is_fitted as check_is_fitted, check_non_negative as check_non_negative
from typing import Any

EPSILON: Any

def norm(x): ...
def trace_dot(X, Y): ...
def non_negative_factorization(X, W: Any | None = ..., H: Any | None = ..., n_components: Any | None = ..., *, init: str = ..., update_H: bool = ..., solver: str = ..., beta_loss: str = ..., tol: float = ..., max_iter: int = ..., alpha: str = ..., alpha_W: float = ..., alpha_H: str = ..., l1_ratio: float = ..., regularization: str = ..., random_state: Any | None = ..., verbose: int = ..., shuffle: bool = ...): ...

class NMF(TransformerMixin, BaseEstimator):
    n_components: Any
    init: Any
    solver: Any
    beta_loss: Any
    tol: Any
    max_iter: Any
    random_state: Any
    alpha: Any
    alpha_W: Any
    alpha_H: Any
    l1_ratio: Any
    verbose: Any
    shuffle: Any
    regularization: Any
    def __init__(self, n_components: Any | None = ..., *, init: str = ..., solver: str = ..., beta_loss: str = ..., tol: float = ..., max_iter: int = ..., random_state: Any | None = ..., alpha: str = ..., alpha_W: float = ..., alpha_H: str = ..., l1_ratio: float = ..., verbose: int = ..., shuffle: bool = ..., regularization: str = ...) -> None: ...
    reconstruction_err_: Any
    n_components_: Any
    components_: Any
    n_iter_: Any
    def fit_transform(self, X, y: Any | None = ..., W: Any | None = ..., H: Any | None = ...): ...
    def fit(self, X, y: Any | None = ..., **params): ...
    def transform(self, X): ...
    def inverse_transform(self, W): ...
