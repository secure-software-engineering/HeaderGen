from .base import BaseEstimator, TransformerMixin
from abc import ABCMeta, abstractmethod
from typing import Any

def johnson_lindenstrauss_min_dim(n_samples, *, eps: float = ...): ...

class BaseRandomProjection(TransformerMixin, BaseEstimator, metaclass=ABCMeta):
    n_components: Any
    eps: Any
    dense_output: Any
    random_state: Any
    @abstractmethod
    def __init__(self, n_components: str = ..., *, eps: float = ..., dense_output: bool = ..., random_state: Any | None = ...): ...
    n_components_: Any
    components_: Any
    def fit(self, X, y: Any | None = ...): ...
    def transform(self, X): ...

class GaussianRandomProjection(BaseRandomProjection):
    def __init__(self, n_components: str = ..., *, eps: float = ..., random_state: Any | None = ...) -> None: ...

class SparseRandomProjection(BaseRandomProjection):
    density: Any
    def __init__(self, n_components: str = ..., *, density: str = ..., eps: float = ..., dense_output: bool = ..., random_state: Any | None = ...) -> None: ...
