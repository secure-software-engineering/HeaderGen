from ..base import BaseEstimator as BaseEstimator
from ..decomposition import PCA as PCA
from ..metrics.pairwise import pairwise_distances as pairwise_distances
from ..neighbors import NearestNeighbors as NearestNeighbors
from ..utils import check_random_state as check_random_state
from ..utils.validation import check_non_negative as check_non_negative
from typing import Any

MACHINE_EPSILON: Any

def trustworthiness(X, X_embedded, *, n_neighbors: int = ..., metric: str = ...): ...

class TSNE(BaseEstimator):
    n_components: Any
    perplexity: Any
    early_exaggeration: Any
    learning_rate: Any
    n_iter: Any
    n_iter_without_progress: Any
    min_grad_norm: Any
    metric: Any
    init: Any
    verbose: Any
    random_state: Any
    method: Any
    angle: Any
    n_jobs: Any
    square_distances: Any
    def __init__(self, n_components: int = ..., *, perplexity: float = ..., early_exaggeration: float = ..., learning_rate: str = ..., n_iter: int = ..., n_iter_without_progress: int = ..., min_grad_norm: float = ..., metric: str = ..., init: str = ..., verbose: int = ..., random_state: Any | None = ..., method: str = ..., angle: float = ..., n_jobs: Any | None = ..., square_distances: str = ...) -> None: ...
    embedding_: Any
    def fit_transform(self, X, y: Any | None = ...): ...
    def fit(self, X, y: Any | None = ...): ...
