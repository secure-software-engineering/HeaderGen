from .._config import config_context as config_context
from ..base import BaseEstimator as BaseEstimator, ClusterMixin as ClusterMixin
from ..metrics.pairwise import pairwise_distances_argmin as pairwise_distances_argmin
from ..neighbors import NearestNeighbors as NearestNeighbors
from ..utils import check_array as check_array, check_random_state as check_random_state, gen_batches as gen_batches
from ..utils.fixes import delayed as delayed
from ..utils.validation import check_is_fitted as check_is_fitted
from typing import Any

def estimate_bandwidth(X, *, quantile: float = ..., n_samples: Any | None = ..., random_state: int = ..., n_jobs: Any | None = ...): ...
def mean_shift(X, *, bandwidth: Any | None = ..., seeds: Any | None = ..., bin_seeding: bool = ..., min_bin_freq: int = ..., cluster_all: bool = ..., max_iter: int = ..., n_jobs: Any | None = ...): ...
def get_bin_seeds(X, bin_size, min_bin_freq: int = ...): ...

class MeanShift(ClusterMixin, BaseEstimator):
    bandwidth: Any
    seeds: Any
    bin_seeding: Any
    cluster_all: Any
    min_bin_freq: Any
    n_jobs: Any
    max_iter: Any
    def __init__(self, *, bandwidth: Any | None = ..., seeds: Any | None = ..., bin_seeding: bool = ..., min_bin_freq: int = ..., cluster_all: bool = ..., n_jobs: Any | None = ..., max_iter: int = ...) -> None: ...
    n_iter_: Any
    def fit(self, X, y: Any | None = ...): ...
    def predict(self, X): ...
