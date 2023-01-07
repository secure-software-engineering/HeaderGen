from sklearn.base import BaseEstimator as BaseEstimator
from sklearn.feature_selection._base import SelectorMixin as SelectorMixin
from sklearn.utils import check_array as check_array
from typing import Any

class StepSelector(SelectorMixin, BaseEstimator):
    step: Any
    def __init__(self, step: int = ...) -> None: ...
    n_input_feats: Any
    def fit(self, X, y: Any | None = ...): ...

support: Any
support_inds: Any
X: Any
Xt: Any
Xinv: Any
y: Any
feature_names: Any
feature_names_t: Any
feature_names_inv: Any

def test_transform_dense() -> None: ...
def test_transform_sparse() -> None: ...
def test_inverse_transform_dense() -> None: ...
def test_inverse_transform_sparse() -> None: ...
def test_get_support() -> None: ...
