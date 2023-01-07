from ..utils import check_array as check_array
from ._base import BaseMixture as BaseMixture
from typing import Any

class BayesianGaussianMixture(BaseMixture):
    covariance_type: Any
    weight_concentration_prior_type: Any
    weight_concentration_prior: Any
    mean_precision_prior: Any
    mean_prior: Any
    degrees_of_freedom_prior: Any
    covariance_prior: Any
    def __init__(self, *, n_components: int = ..., covariance_type: str = ..., tol: float = ..., reg_covar: float = ..., max_iter: int = ..., n_init: int = ..., init_params: str = ..., weight_concentration_prior_type: str = ..., weight_concentration_prior: Any | None = ..., mean_precision_prior: Any | None = ..., mean_prior: Any | None = ..., degrees_of_freedom_prior: Any | None = ..., covariance_prior: Any | None = ..., random_state: Any | None = ..., warm_start: bool = ..., verbose: int = ..., verbose_interval: int = ...) -> None: ...
