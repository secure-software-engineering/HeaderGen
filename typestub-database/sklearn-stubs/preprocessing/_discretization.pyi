from . import OneHotEncoder as OneHotEncoder
from ..base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin
from ..utils.validation import check_array as check_array, check_is_fitted as check_is_fitted
from typing import Any

class KBinsDiscretizer(TransformerMixin, BaseEstimator):
    n_bins: Any
    encode: Any
    strategy: Any
    dtype: Any
    def __init__(self, n_bins: int = ..., *, encode: str = ..., strategy: str = ..., dtype: Any | None = ...) -> None: ...
    bin_edges_: Any
    n_bins_: Any
    def fit(self, X, y: Any | None = ...): ...
    def transform(self, X): ...
    def inverse_transform(self, Xt): ...
    def get_feature_names_out(self, input_features: Any | None = ...): ...
