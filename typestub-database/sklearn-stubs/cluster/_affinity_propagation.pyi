from .._config import config_context as config_context
from ..base import BaseEstimator as BaseEstimator, ClusterMixin as ClusterMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..metrics import euclidean_distances as euclidean_distances, pairwise_distances_argmin as pairwise_distances_argmin
from ..utils import as_float_array as as_float_array, check_random_state as check_random_state, check_scalar as check_scalar
from ..utils.deprecation import deprecated as deprecated
from ..utils.validation import check_is_fitted as check_is_fitted
from typing import Any

def affinity_propagation(S, *, preference: Any | None = ..., convergence_iter: int = ..., max_iter: int = ..., damping: float = ..., copy: bool = ..., verbose: bool = ..., return_n_iter: bool = ..., random_state: Any | None = ...): ...

class AffinityPropagation(ClusterMixin, BaseEstimator):
    damping: Any
    max_iter: Any
    convergence_iter: Any
    copy: Any
    verbose: Any
    preference: Any
    affinity: Any
    random_state: Any
    def __init__(self, *, damping: float = ..., max_iter: int = ..., convergence_iter: int = ..., copy: bool = ..., preference: Any | None = ..., affinity: str = ..., verbose: bool = ..., random_state: Any | None = ...) -> None: ...
    affinity_matrix_: Any
    cluster_centers_: Any
    def fit(self, X, y: Any | None = ...): ...
    def predict(self, X): ...
    def fit_predict(self, X, y: Any | None = ...): ...
