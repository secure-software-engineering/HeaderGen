from ..base import BaseEstimator as BaseEstimator
from ..utils import check_random_state as check_random_state
from ..utils.extmath import row_norms as row_norms
from ..utils.validation import check_is_fitted as check_is_fitted
from ._ball_tree import BallTree as BallTree, DTYPE as DTYPE
from ._kd_tree import KDTree as KDTree
from typing import Any

VALID_KERNELS: Any
TREE_DICT: Any

class KernelDensity(BaseEstimator):
    algorithm: Any
    bandwidth: Any
    kernel: Any
    metric: Any
    atol: Any
    rtol: Any
    breadth_first: Any
    leaf_size: Any
    metric_params: Any
    def __init__(self, *, bandwidth: float = ..., algorithm: str = ..., kernel: str = ..., metric: str = ..., atol: int = ..., rtol: int = ..., breadth_first: bool = ..., leaf_size: int = ..., metric_params: Any | None = ...) -> None: ...
    tree_: Any
    def fit(self, X, y: Any | None = ..., sample_weight: Any | None = ...): ...
    def score_samples(self, X): ...
    def score(self, X, y: Any | None = ...): ...
    def sample(self, n_samples: int = ..., random_state: Any | None = ...): ...
