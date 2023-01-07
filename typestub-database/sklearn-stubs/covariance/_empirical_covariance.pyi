from .. import config_context as config_context
from ..base import BaseEstimator as BaseEstimator
from ..metrics.pairwise import pairwise_distances as pairwise_distances
from ..utils import check_array as check_array
from ..utils.extmath import fast_logdet as fast_logdet
from typing import Any

def log_likelihood(emp_cov, precision): ...
def empirical_covariance(X, *, assume_centered: bool = ...): ...

class EmpiricalCovariance(BaseEstimator):
    store_precision: Any
    assume_centered: Any
    def __init__(self, *, store_precision: bool = ..., assume_centered: bool = ...) -> None: ...
    def get_precision(self): ...
    location_: Any
    def fit(self, X, y: Any | None = ...): ...
    def score(self, X_test, y: Any | None = ...): ...
    def error_norm(self, comp_cov, norm: str = ..., scaling: bool = ..., squared: bool = ...): ...
    def mahalanobis(self, X): ...
