from ...base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin
from ...utils import check_array as check_array, check_random_state as check_random_state
from ...utils.fixes import percentile as percentile
from ...utils.validation import check_is_fitted as check_is_fitted
from ._bitset import set_bitset_memoryview as set_bitset_memoryview
from .common import ALMOST_INF as ALMOST_INF, X_BINNED_DTYPE as X_BINNED_DTYPE, X_BITSET_INNER_DTYPE as X_BITSET_INNER_DTYPE, X_DTYPE as X_DTYPE
from typing import Any

class _BinMapper(TransformerMixin, BaseEstimator):
    n_bins: Any
    subsample: Any
    is_categorical: Any
    known_categories: Any
    random_state: Any
    n_threads: Any
    def __init__(self, n_bins: int = ..., subsample=..., is_categorical: Any | None = ..., known_categories: Any | None = ..., random_state: Any | None = ..., n_threads: Any | None = ...) -> None: ...
    is_categorical_: Any
    missing_values_bin_idx_: Any
    bin_thresholds_: Any
    n_bins_non_missing_: Any
    def fit(self, X, y: Any | None = ...): ...
    def transform(self, X): ...
    def make_known_categories_bitsets(self): ...
