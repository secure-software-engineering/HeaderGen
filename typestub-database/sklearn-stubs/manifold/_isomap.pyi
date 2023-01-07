from ..base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin
from ..decomposition import KernelPCA as KernelPCA
from ..neighbors import NearestNeighbors as NearestNeighbors, kneighbors_graph as kneighbors_graph
from ..preprocessing import KernelCenterer as KernelCenterer
from ..utils.validation import check_is_fitted as check_is_fitted
from typing import Any

class Isomap(TransformerMixin, BaseEstimator):
    n_neighbors: Any
    n_components: Any
    eigen_solver: Any
    tol: Any
    max_iter: Any
    path_method: Any
    neighbors_algorithm: Any
    n_jobs: Any
    metric: Any
    p: Any
    metric_params: Any
    def __init__(self, *, n_neighbors: int = ..., n_components: int = ..., eigen_solver: str = ..., tol: int = ..., max_iter: Any | None = ..., path_method: str = ..., neighbors_algorithm: str = ..., n_jobs: Any | None = ..., metric: str = ..., p: int = ..., metric_params: Any | None = ...) -> None: ...
    def reconstruction_error(self): ...
    def fit(self, X, y: Any | None = ...): ...
    def fit_transform(self, X, y: Any | None = ...): ...
    def transform(self, X): ...
