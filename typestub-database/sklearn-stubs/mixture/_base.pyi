from .. import cluster as cluster
from ..base import BaseEstimator as BaseEstimator, DensityMixin as DensityMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils import check_random_state as check_random_state
from ..utils.validation import check_is_fitted as check_is_fitted
from abc import ABCMeta
from typing import Any

class BaseMixture(DensityMixin, BaseEstimator, metaclass=ABCMeta):
    n_components: Any
    tol: Any
    reg_covar: Any
    max_iter: Any
    n_init: Any
    init_params: Any
    random_state: Any
    warm_start: Any
    verbose: Any
    verbose_interval: Any
    def __init__(self, n_components, tol, reg_covar, max_iter, n_init, init_params, random_state, warm_start, verbose, verbose_interval) -> None: ...
    def fit(self, X, y: Any | None = ...): ...
    converged_: bool
    n_iter_: Any
    lower_bound_: Any
    def fit_predict(self, X, y: Any | None = ...): ...
    def score_samples(self, X): ...
    def score(self, X, y: Any | None = ...): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def sample(self, n_samples: int = ...): ...
