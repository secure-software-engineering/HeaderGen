from ..base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils import check_random_state as check_random_state
from ..utils.extmath import fast_logdet as fast_logdet, randomized_svd as randomized_svd, squared_norm as squared_norm
from ..utils.validation import check_is_fitted as check_is_fitted
from typing import Any

class FactorAnalysis(TransformerMixin, BaseEstimator):
    n_components: Any
    copy: Any
    tol: Any
    max_iter: Any
    svd_method: Any
    noise_variance_init: Any
    iterated_power: Any
    random_state: Any
    rotation: Any
    def __init__(self, n_components: Any | None = ..., *, tol: float = ..., copy: bool = ..., max_iter: int = ..., noise_variance_init: Any | None = ..., svd_method: str = ..., iterated_power: int = ..., rotation: Any | None = ..., random_state: int = ...) -> None: ...
    mean_: Any
    components_: Any
    noise_variance_: Any
    loglike_: Any
    n_iter_: Any
    def fit(self, X, y: Any | None = ...): ...
    def transform(self, X): ...
    def get_covariance(self): ...
    def get_precision(self): ...
    def score_samples(self, X): ...
    def score(self, X, y: Any | None = ...): ...
