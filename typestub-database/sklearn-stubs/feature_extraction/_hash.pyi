from ..base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin
from ..utils import IS_PYPY as IS_PYPY
from typing import Any

class FeatureHasher(TransformerMixin, BaseEstimator):
    dtype: Any
    input_type: Any
    n_features: Any
    alternate_sign: Any
    def __init__(self, n_features=..., *, input_type: str = ..., dtype=..., alternate_sign: bool = ...) -> None: ...
    def fit(self, X: Any | None = ..., y: Any | None = ...): ...
    def transform(self, raw_X): ...
