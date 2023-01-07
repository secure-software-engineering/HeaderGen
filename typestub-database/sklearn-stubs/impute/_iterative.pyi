from ..base import clone as clone
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..preprocessing import normalize as normalize
from ..utils import check_array as check_array, check_random_state as check_random_state, is_scalar_nan as is_scalar_nan
from ..utils.validation import FLOAT_DTYPES as FLOAT_DTYPES, check_is_fitted as check_is_fitted
from ._base import SimpleImputer as SimpleImputer, _BaseImputer
from typing import Any, NamedTuple

class _ImputerTriplet(NamedTuple):
    feat_idx: Any
    neighbor_feat_idx: Any
    estimator: Any

class IterativeImputer(_BaseImputer):
    estimator: Any
    sample_posterior: Any
    max_iter: Any
    tol: Any
    n_nearest_features: Any
    initial_strategy: Any
    imputation_order: Any
    skip_complete: Any
    min_value: Any
    max_value: Any
    verbose: Any
    random_state: Any
    def __init__(self, estimator: Any | None = ..., *, missing_values=..., sample_posterior: bool = ..., max_iter: int = ..., tol: float = ..., n_nearest_features: Any | None = ..., initial_strategy: str = ..., imputation_order: str = ..., skip_complete: bool = ..., min_value=..., max_value=..., verbose: int = ..., random_state: Any | None = ..., add_indicator: bool = ...) -> None: ...
    random_state_: Any
    imputation_sequence_: Any
    initial_imputer_: Any
    n_iter_: int
    n_features_with_missing_: Any
    def fit_transform(self, X, y: Any | None = ...): ...
    def transform(self, X): ...
    def fit(self, X, y: Any | None = ...): ...
