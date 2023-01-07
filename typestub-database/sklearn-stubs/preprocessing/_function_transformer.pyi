from ..base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin
from ..utils.validation import check_array as check_array
from typing import Any

class FunctionTransformer(TransformerMixin, BaseEstimator):
    func: Any
    inverse_func: Any
    validate: Any
    accept_sparse: Any
    check_inverse: Any
    kw_args: Any
    inv_kw_args: Any
    def __init__(self, func: Any | None = ..., inverse_func: Any | None = ..., *, validate: bool = ..., accept_sparse: bool = ..., check_inverse: bool = ..., kw_args: Any | None = ..., inv_kw_args: Any | None = ...) -> None: ...
    def fit(self, X, y: Any | None = ...): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
    def __sklearn_is_fitted__(self): ...
