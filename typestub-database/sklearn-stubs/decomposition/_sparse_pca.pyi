from ..base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin
from ..linear_model import ridge_regression as ridge_regression
from ..utils import check_random_state as check_random_state
from ..utils.validation import check_is_fitted as check_is_fitted
from ._dict_learning import dict_learning as dict_learning, dict_learning_online as dict_learning_online
from typing import Any

class SparsePCA(TransformerMixin, BaseEstimator):
    n_components: Any
    alpha: Any
    ridge_alpha: Any
    max_iter: Any
    tol: Any
    method: Any
    n_jobs: Any
    U_init: Any
    V_init: Any
    verbose: Any
    random_state: Any
    def __init__(self, n_components: Any | None = ..., *, alpha: int = ..., ridge_alpha: float = ..., max_iter: int = ..., tol: float = ..., method: str = ..., n_jobs: Any | None = ..., U_init: Any | None = ..., V_init: Any | None = ..., verbose: bool = ..., random_state: Any | None = ...) -> None: ...
    mean_: Any
    components_: Any
    n_components_: Any
    error_: Any
    def fit(self, X, y: Any | None = ...): ...
    def transform(self, X): ...

class MiniBatchSparsePCA(SparsePCA):
    n_iter: Any
    callback: Any
    batch_size: Any
    shuffle: Any
    def __init__(self, n_components: Any | None = ..., *, alpha: int = ..., ridge_alpha: float = ..., n_iter: int = ..., callback: Any | None = ..., batch_size: int = ..., verbose: bool = ..., shuffle: bool = ..., n_jobs: Any | None = ..., method: str = ..., random_state: Any | None = ...) -> None: ...
    mean_: Any
    components_: Any
    n_components_: Any
    def fit(self, X, y: Any | None = ...): ...
