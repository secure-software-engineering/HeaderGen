from ..base import BaseEstimator as BaseEstimator, ClusterMixin as ClusterMixin
from ..manifold import spectral_embedding as spectral_embedding
from ..metrics.pairwise import pairwise_kernels as pairwise_kernels
from ..neighbors import NearestNeighbors as NearestNeighbors, kneighbors_graph as kneighbors_graph
from ..utils import as_float_array as as_float_array, check_random_state as check_random_state
from ..utils.deprecation import deprecated as deprecated
from ._kmeans import k_means as k_means
from typing import Any

def discretize(vectors, *, copy: bool = ..., max_svd_restarts: int = ..., n_iter_max: int = ..., random_state: Any | None = ...): ...
def spectral_clustering(affinity, *, n_clusters: int = ..., n_components: Any | None = ..., eigen_solver: Any | None = ..., random_state: Any | None = ..., n_init: int = ..., eigen_tol: float = ..., assign_labels: str = ..., verbose: bool = ...): ...

class SpectralClustering(ClusterMixin, BaseEstimator):
    n_clusters: Any
    eigen_solver: Any
    n_components: Any
    random_state: Any
    n_init: Any
    gamma: Any
    affinity: Any
    n_neighbors: Any
    eigen_tol: Any
    assign_labels: Any
    degree: Any
    coef0: Any
    kernel_params: Any
    n_jobs: Any
    verbose: Any
    def __init__(self, n_clusters: int = ..., *, eigen_solver: Any | None = ..., n_components: Any | None = ..., random_state: Any | None = ..., n_init: int = ..., gamma: float = ..., affinity: str = ..., n_neighbors: int = ..., eigen_tol: float = ..., assign_labels: str = ..., degree: int = ..., coef0: int = ..., kernel_params: Any | None = ..., n_jobs: Any | None = ..., verbose: bool = ...) -> None: ...
    affinity_matrix_: Any
    labels_: Any
    def fit(self, X, y: Any | None = ...): ...
    def fit_predict(self, X, y: Any | None = ...): ...
