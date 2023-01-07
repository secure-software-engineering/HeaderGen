from . import AgglomerativeClustering as AgglomerativeClustering
from .._config import config_context as config_context
from ..base import BaseEstimator as BaseEstimator, ClusterMixin as ClusterMixin, TransformerMixin as TransformerMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..metrics import pairwise_distances_argmin as pairwise_distances_argmin
from ..metrics.pairwise import euclidean_distances as euclidean_distances
from ..utils import deprecated as deprecated
from ..utils.extmath import row_norms as row_norms
from ..utils.validation import check_is_fitted as check_is_fitted
from typing import Any

class _CFNode:
    threshold: Any
    branching_factor: Any
    is_leaf: Any
    n_features: Any
    subclusters_: Any
    init_centroids_: Any
    init_sq_norm_: Any
    squared_norm_: Any
    prev_leaf_: Any
    next_leaf_: Any
    def __init__(self, threshold, branching_factor, is_leaf, n_features) -> None: ...
    centroids_: Any
    def append_subcluster(self, subcluster) -> None: ...
    def update_split_subclusters(self, subcluster, new_subcluster1, new_subcluster2) -> None: ...
    def insert_cf_subcluster(self, subcluster): ...

class _CFSubcluster:
    n_samples_: int
    squared_sum_: float
    centroid_: int
    child_: Any
    def __init__(self, *, linear_sum: Any | None = ...) -> None: ...
    sq_norm_: Any
    def update(self, subcluster) -> None: ...
    def merge_subcluster(self, nominee_cluster, threshold): ...
    @property
    def radius(self): ...

class Birch(ClusterMixin, TransformerMixin, BaseEstimator):
    threshold: Any
    branching_factor: Any
    n_clusters: Any
    compute_labels: Any
    copy: Any
    def __init__(self, *, threshold: float = ..., branching_factor: int = ..., n_clusters: int = ..., compute_labels: bool = ..., copy: bool = ...) -> None: ...
    @property
    def fit_(self): ...
    @property
    def partial_fit_(self): ...
    def fit(self, X, y: Any | None = ...): ...
    def partial_fit(self, X: Any | None = ..., y: Any | None = ...): ...
    def predict(self, X): ...
    def transform(self, X): ...
