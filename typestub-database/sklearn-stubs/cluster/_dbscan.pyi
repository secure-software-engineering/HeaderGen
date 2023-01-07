from ..base import BaseEstimator as BaseEstimator, ClusterMixin as ClusterMixin
from ..neighbors import NearestNeighbors as NearestNeighbors
from ._dbscan_inner import dbscan_inner as dbscan_inner
from typing import Any

def dbscan(X, eps: float = ..., *, min_samples: int = ..., metric: str = ..., metric_params: Any | None = ..., algorithm: str = ..., leaf_size: int = ..., p: int = ..., sample_weight: Any | None = ..., n_jobs: Any | None = ...): ...

class DBSCAN(ClusterMixin, BaseEstimator):
    eps: Any
    min_samples: Any
    metric: Any
    metric_params: Any
    algorithm: Any
    leaf_size: Any
    p: Any
    n_jobs: Any
    def __init__(self, eps: float = ..., *, min_samples: int = ..., metric: str = ..., metric_params: Any | None = ..., algorithm: str = ..., leaf_size: int = ..., p: Any | None = ..., n_jobs: Any | None = ...) -> None: ...
    core_sample_indices_: Any
    labels_: Any
    components_: Any
    def fit(self, X, y: Any | None = ..., sample_weight: Any | None = ...): ...
    def fit_predict(self, X, y: Any | None = ..., sample_weight: Any | None = ...): ...
