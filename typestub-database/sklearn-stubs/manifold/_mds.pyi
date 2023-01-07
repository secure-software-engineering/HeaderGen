from ..base import BaseEstimator as BaseEstimator
from ..isotonic import IsotonicRegression as IsotonicRegression
from ..metrics import euclidean_distances as euclidean_distances
from ..utils import check_array as check_array, check_random_state as check_random_state, check_symmetric as check_symmetric
from ..utils.deprecation import deprecated as deprecated
from ..utils.fixes import delayed as delayed
from typing import Any

def smacof(dissimilarities, *, metric: bool = ..., n_components: int = ..., init: Any | None = ..., n_init: int = ..., n_jobs: Any | None = ..., max_iter: int = ..., verbose: int = ..., eps: float = ..., random_state: Any | None = ..., return_n_iter: bool = ...): ...

class MDS(BaseEstimator):
    n_components: Any
    dissimilarity: Any
    metric: Any
    n_init: Any
    max_iter: Any
    eps: Any
    verbose: Any
    n_jobs: Any
    random_state: Any
    def __init__(self, n_components: int = ..., *, metric: bool = ..., n_init: int = ..., max_iter: int = ..., verbose: int = ..., eps: float = ..., n_jobs: Any | None = ..., random_state: Any | None = ..., dissimilarity: str = ...) -> None: ...
    def fit(self, X, y: Any | None = ..., init: Any | None = ...): ...
    dissimilarity_matrix_: Any
    def fit_transform(self, X, y: Any | None = ..., init: Any | None = ...): ...
