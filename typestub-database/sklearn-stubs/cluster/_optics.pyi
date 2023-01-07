from ..base import BaseEstimator as BaseEstimator, ClusterMixin as ClusterMixin
from ..exceptions import DataConversionWarning as DataConversionWarning
from ..metrics import pairwise_distances as pairwise_distances
from ..metrics.pairwise import PAIRWISE_BOOLEAN_FUNCTIONS as PAIRWISE_BOOLEAN_FUNCTIONS
from ..neighbors import NearestNeighbors as NearestNeighbors
from ..utils import gen_batches as gen_batches, get_chunk_n_rows as get_chunk_n_rows
from ..utils.validation import check_memory as check_memory
from typing import Any

class OPTICS(ClusterMixin, BaseEstimator):
    max_eps: Any
    min_samples: Any
    min_cluster_size: Any
    algorithm: Any
    metric: Any
    metric_params: Any
    p: Any
    leaf_size: Any
    cluster_method: Any
    eps: Any
    xi: Any
    predecessor_correction: Any
    memory: Any
    n_jobs: Any
    def __init__(self, *, min_samples: int = ..., max_eps=..., metric: str = ..., p: int = ..., metric_params: Any | None = ..., cluster_method: str = ..., eps: Any | None = ..., xi: float = ..., predecessor_correction: bool = ..., min_cluster_size: Any | None = ..., algorithm: str = ..., leaf_size: int = ..., memory: Any | None = ..., n_jobs: Any | None = ...) -> None: ...
    cluster_hierarchy_: Any
    labels_: Any
    def fit(self, X, y: Any | None = ...): ...

def compute_optics_graph(X, min_samples, max_eps, metric, p, metric_params, algorithm, leaf_size, n_jobs): ...
def cluster_optics_dbscan(reachability, core_distances, ordering, eps): ...
def cluster_optics_xi(reachability, predecessor, ordering, min_samples, *, min_cluster_size: Any | None = ..., xi: float = ..., predecessor_correction: bool = ...): ...
