from ..utils import check_array as check_array
from ..utils.extmath import row_norms as row_norms
from ._base import BaseMixture as BaseMixture
from typing import Any

class GaussianMixture(BaseMixture):
    covariance_type: Any
    weights_init: Any
    means_init: Any
    precisions_init: Any
    def __init__(self, n_components: int = ..., *, covariance_type: str = ..., tol: float = ..., reg_covar: float = ..., max_iter: int = ..., n_init: int = ..., init_params: str = ..., weights_init: Any | None = ..., means_init: Any | None = ..., precisions_init: Any | None = ..., random_state: Any | None = ..., warm_start: bool = ..., verbose: int = ..., verbose_interval: int = ...) -> None: ...
    def bic(self, X): ...
    def aic(self, X): ...
