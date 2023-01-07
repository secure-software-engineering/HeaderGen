from ..base import BaseEstimator as BaseEstimator, ClusterMixin as ClusterMixin, TransformerMixin as TransformerMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..metrics.pairwise import euclidean_distances as euclidean_distances
from ..utils import check_array as check_array, check_random_state as check_random_state, deprecated as deprecated
from ..utils._readonly_array_wrapper import ReadonlyArrayWrapper as ReadonlyArrayWrapper
from ..utils.extmath import row_norms as row_norms, stable_cumsum as stable_cumsum
from ..utils.fixes import threadpool_info as threadpool_info, threadpool_limits as threadpool_limits
from ..utils.sparsefuncs import mean_variance_axis as mean_variance_axis
from ..utils.sparsefuncs_fast import assign_rows_csr as assign_rows_csr
from ..utils.validation import check_is_fitted as check_is_fitted
from ._k_means_common import CHUNK_SIZE as CHUNK_SIZE
from ._k_means_elkan import elkan_iter_chunked_dense as elkan_iter_chunked_dense, elkan_iter_chunked_sparse as elkan_iter_chunked_sparse, init_bounds_dense as init_bounds_dense, init_bounds_sparse as init_bounds_sparse
from ._k_means_lloyd import lloyd_iter_chunked_dense as lloyd_iter_chunked_dense, lloyd_iter_chunked_sparse as lloyd_iter_chunked_sparse
from typing import Any

def kmeans_plusplus(X, n_clusters, *, x_squared_norms: Any | None = ..., random_state: Any | None = ..., n_local_trials: Any | None = ...): ...
def k_means(X, n_clusters, *, sample_weight: Any | None = ..., init: str = ..., n_init: int = ..., max_iter: int = ..., verbose: bool = ..., tol: float = ..., random_state: Any | None = ..., copy_x: bool = ..., algorithm: str = ..., return_n_iter: bool = ...): ...

class KMeans(TransformerMixin, ClusterMixin, BaseEstimator):
    n_clusters: Any
    init: Any
    max_iter: Any
    tol: Any
    n_init: Any
    verbose: Any
    random_state: Any
    copy_x: Any
    algorithm: Any
    def __init__(self, n_clusters: int = ..., *, init: str = ..., n_init: int = ..., max_iter: int = ..., tol: float = ..., verbose: int = ..., random_state: Any | None = ..., copy_x: bool = ..., algorithm: str = ...) -> None: ...
    cluster_centers_: Any
    labels_: Any
    inertia_: Any
    n_iter_: Any
    def fit(self, X, y: Any | None = ..., sample_weight: Any | None = ...): ...
    def fit_predict(self, X, y: Any | None = ..., sample_weight: Any | None = ...): ...
    def fit_transform(self, X, y: Any | None = ..., sample_weight: Any | None = ...): ...
    def transform(self, X): ...
    def predict(self, X, sample_weight: Any | None = ...): ...
    def score(self, X, y: Any | None = ..., sample_weight: Any | None = ...): ...

class MiniBatchKMeans(KMeans):
    max_no_improvement: Any
    batch_size: Any
    compute_labels: Any
    init_size: Any
    reassignment_ratio: Any
    def __init__(self, n_clusters: int = ..., *, init: str = ..., max_iter: int = ..., batch_size: int = ..., verbose: int = ..., compute_labels: bool = ..., random_state: Any | None = ..., tol: float = ..., max_no_improvement: int = ..., init_size: Any | None = ..., n_init: int = ..., reassignment_ratio: float = ...) -> None: ...
    @property
    def counts_(self): ...
    @property
    def init_size_(self): ...
    @property
    def random_state_(self): ...
    cluster_centers_: Any
    n_steps_: Any
    n_iter_: Any
    inertia_: Any
    def fit(self, X, y: Any | None = ..., sample_weight: Any | None = ...): ...
    def partial_fit(self, X, y: Any | None = ..., sample_weight: Any | None = ...): ...
    def predict(self, X, sample_weight: Any | None = ...): ...
