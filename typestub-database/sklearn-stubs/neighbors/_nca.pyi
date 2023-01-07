from ..base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin
from ..decomposition import PCA as PCA
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..metrics import pairwise_distances as pairwise_distances
from ..preprocessing import LabelEncoder as LabelEncoder
from ..utils.extmath import softmax as softmax
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.random import check_random_state as check_random_state
from ..utils.validation import check_array as check_array, check_is_fitted as check_is_fitted, check_scalar as check_scalar
from typing import Any

class NeighborhoodComponentsAnalysis(TransformerMixin, BaseEstimator):
    n_components: Any
    init: Any
    warm_start: Any
    max_iter: Any
    tol: Any
    callback: Any
    verbose: Any
    random_state: Any
    def __init__(self, n_components: Any | None = ..., *, init: str = ..., warm_start: bool = ..., max_iter: int = ..., tol: float = ..., callback: Any | None = ..., verbose: int = ..., random_state: Any | None = ...) -> None: ...
    random_state_: Any
    n_iter_: int
    components_: Any
    def fit(self, X, y): ...
    def transform(self, X): ...
