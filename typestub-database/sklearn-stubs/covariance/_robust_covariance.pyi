from . import EmpiricalCovariance as EmpiricalCovariance, empirical_covariance as empirical_covariance
from ..utils import check_array as check_array, check_random_state as check_random_state
from ..utils.extmath import fast_logdet as fast_logdet
from typing import Any

def c_step(X, n_support, remaining_iterations: int = ..., initial_estimates: Any | None = ..., verbose: bool = ..., cov_computation_method=..., random_state: Any | None = ...): ...
def select_candidates(X, n_support, n_trials, select: int = ..., n_iter: int = ..., verbose: bool = ..., cov_computation_method=..., random_state: Any | None = ...): ...
def fast_mcd(X, support_fraction: Any | None = ..., cov_computation_method=..., random_state: Any | None = ...): ...

class MinCovDet(EmpiricalCovariance):
    store_precision: Any
    assume_centered: Any
    support_fraction: Any
    random_state: Any
    def __init__(self, *, store_precision: bool = ..., assume_centered: bool = ..., support_fraction: Any | None = ..., random_state: Any | None = ...) -> None: ...
    raw_location_: Any
    raw_covariance_: Any
    raw_support_: Any
    location_: Any
    support_: Any
    dist_: Any
    def fit(self, X, y: Any | None = ...): ...
    def correct_covariance(self, data): ...
    def reweight_covariance(self, data): ...
