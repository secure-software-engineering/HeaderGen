import abc
from ..base import BaseEstimator as BaseEstimator
from ..preprocessing import LabelBinarizer as LabelBinarizer
from ..utils import as_float_array as as_float_array, check_X_y as check_X_y, check_array as check_array, safe_mask as safe_mask, safe_sqr as safe_sqr
from ..utils.extmath import row_norms as row_norms, safe_sparse_dot as safe_sparse_dot
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import SelectorMixin as SelectorMixin
from typing import Any

def f_oneway(*args): ...
def f_classif(X, y): ...
def chi2(X, y): ...
def r_regression(X, y, *, center: bool = ...): ...
def f_regression(X, y, *, center: bool = ...): ...

class _BaseFilter(SelectorMixin, BaseEstimator, metaclass=abc.ABCMeta):
    score_func: Any
    def __init__(self, score_func) -> None: ...
    pvalues_: Any
    scores_: Any
    def fit(self, X, y): ...

class SelectPercentile(_BaseFilter):
    percentile: Any
    def __init__(self, score_func=..., *, percentile: int = ...) -> None: ...

class SelectKBest(_BaseFilter):
    k: Any
    def __init__(self, score_func=..., *, k: int = ...) -> None: ...

class SelectFpr(_BaseFilter):
    alpha: Any
    def __init__(self, score_func=..., *, alpha: float = ...) -> None: ...

class SelectFdr(_BaseFilter):
    alpha: Any
    def __init__(self, score_func=..., *, alpha: float = ...) -> None: ...

class SelectFwe(_BaseFilter):
    alpha: Any
    def __init__(self, score_func=..., *, alpha: float = ...) -> None: ...

class GenericUnivariateSelect(_BaseFilter):
    mode: Any
    param: Any
    def __init__(self, score_func=..., *, mode: str = ..., param: float = ...) -> None: ...
