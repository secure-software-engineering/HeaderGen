from ..base import BaseEstimator, TransformerMixin
from typing import Any

class TruncatedSVD(TransformerMixin, BaseEstimator):
    algorithm: Any
    n_components: Any
    n_iter: Any
    random_state: Any
    tol: Any
    def __init__(self, n_components: int = ..., *, algorithm: str = ..., n_iter: int = ..., random_state: Any | None = ..., tol: float = ...) -> None: ...
    def fit(self, X, y: Any | None = ...): ...
    components_: Any
    explained_variance_: Any
    explained_variance_ratio_: Any
    singular_values_: Any
    def fit_transform(self, X, y: Any | None = ...): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
