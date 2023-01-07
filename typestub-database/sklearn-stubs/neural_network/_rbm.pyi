from ..base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin
from ..utils import check_random_state as check_random_state, gen_even_slices as gen_even_slices
from ..utils.extmath import log_logistic as log_logistic, safe_sparse_dot as safe_sparse_dot
from ..utils.validation import check_is_fitted as check_is_fitted
from typing import Any

class BernoulliRBM(TransformerMixin, BaseEstimator):
    n_components: Any
    learning_rate: Any
    batch_size: Any
    n_iter: Any
    verbose: Any
    random_state: Any
    def __init__(self, n_components: int = ..., *, learning_rate: float = ..., batch_size: int = ..., n_iter: int = ..., verbose: int = ..., random_state: Any | None = ...) -> None: ...
    def transform(self, X): ...
    random_state_: Any
    def gibbs(self, v): ...
    components_: Any
    intercept_hidden_: Any
    intercept_visible_: Any
    h_samples_: Any
    def partial_fit(self, X, y: Any | None = ...) -> None: ...
    def score_samples(self, X): ...
    def fit(self, X, y: Any | None = ...): ...
