from ..base import BaseEstimator as BaseEstimator, ClassifierMixin as ClassifierMixin
from .validation import check_array as check_array, check_is_fitted as check_is_fitted
from typing import Any

class ArraySlicingWrapper:
    array: Any
    def __init__(self, array) -> None: ...
    def __getitem__(self, aslice): ...

class MockDataFrame:
    array: Any
    values: Any
    shape: Any
    ndim: Any
    iloc: Any
    def __init__(self, array) -> None: ...
    def __len__(self): ...
    def __array__(self, dtype: Any | None = ...): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def take(self, indices, axis: int = ...): ...

class CheckingClassifier(ClassifierMixin, BaseEstimator):
    check_y: Any
    check_y_params: Any
    check_X: Any
    check_X_params: Any
    methods_to_check: Any
    foo_param: Any
    expected_fit_params: Any
    def __init__(self, *, check_y: Any | None = ..., check_y_params: Any | None = ..., check_X: Any | None = ..., check_X_params: Any | None = ..., methods_to_check: str = ..., foo_param: int = ..., expected_fit_params: Any | None = ...) -> None: ...
    n_features_in_: Any
    classes_: Any
    def fit(self, X, y, **fit_params): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def decision_function(self, X): ...
    def score(self, X: Any | None = ..., Y: Any | None = ...): ...

class NoSampleWeightWrapper(BaseEstimator):
    est: Any
    def __init__(self, est: Any | None = ...) -> None: ...
    def fit(self, X, y): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
