from ..base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin, _UnstableArchMixin
from ..neighbors import NearestNeighbors as NearestNeighbors
from ..utils import check_array as check_array, check_random_state as check_random_state
from ..utils.extmath import stable_cumsum as stable_cumsum
from ..utils.validation import FLOAT_DTYPES as FLOAT_DTYPES, check_is_fitted as check_is_fitted
from typing import Any

def barycenter_weights(X, Y, indices, reg: float = ...): ...
def barycenter_kneighbors_graph(X, n_neighbors, reg: float = ..., n_jobs: Any | None = ...): ...
def null_space(M, k, k_skip: int = ..., eigen_solver: str = ..., tol: float = ..., max_iter: int = ..., random_state: Any | None = ...): ...
def locally_linear_embedding(X, n_neighbors, n_components, *, reg: float = ..., eigen_solver: str = ..., tol: float = ..., max_iter: int = ..., method: str = ..., hessian_tol: float = ..., modified_tol: float = ..., random_state: Any | None = ..., n_jobs: Any | None = ...): ...

class LocallyLinearEmbedding(TransformerMixin, _UnstableArchMixin, BaseEstimator):
    n_neighbors: Any
    n_components: Any
    reg: Any
    eigen_solver: Any
    tol: Any
    max_iter: Any
    method: Any
    hessian_tol: Any
    modified_tol: Any
    random_state: Any
    neighbors_algorithm: Any
    n_jobs: Any
    def __init__(self, *, n_neighbors: int = ..., n_components: int = ..., reg: float = ..., eigen_solver: str = ..., tol: float = ..., max_iter: int = ..., method: str = ..., hessian_tol: float = ..., modified_tol: float = ..., neighbors_algorithm: str = ..., random_state: Any | None = ..., n_jobs: Any | None = ...) -> None: ...
    def fit(self, X, y: Any | None = ...): ...
    def fit_transform(self, X, y: Any | None = ...): ...
    def transform(self, X): ...
