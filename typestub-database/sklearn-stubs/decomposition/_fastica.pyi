from ..base import BaseEstimator, TransformerMixin
from typing import Any

def fastica(X, n_components: Any | None = ..., *, algorithm: str = ..., whiten: bool = ..., fun: str = ..., fun_args: Any | None = ..., max_iter: int = ..., tol: float = ..., w_init: Any | None = ..., random_state: Any | None = ..., return_X_mean: bool = ..., compute_sources: bool = ..., return_n_iter: bool = ...): ...

class FastICA(TransformerMixin, BaseEstimator):
    n_components: Any
    algorithm: Any
    whiten: Any
    fun: Any
    fun_args: Any
    max_iter: Any
    tol: Any
    w_init: Any
    random_state: Any
    def __init__(self, n_components: Any | None = ..., *, algorithm: str = ..., whiten: bool = ..., fun: str = ..., fun_args: Any | None = ..., max_iter: int = ..., tol: float = ..., w_init: Any | None = ..., random_state: Any | None = ...) -> None: ...
    def fit_transform(self, X, y: Any | None = ...): ...
    def fit(self, X, y: Any | None = ...): ...
    def transform(self, X, copy: bool = ...): ...
    def inverse_transform(self, X, copy: bool = ...): ...
