from ..base import BaseEstimator, RegressorMixin
from typing import Any

class TransformedTargetRegressor(RegressorMixin, BaseEstimator):
    regressor: Any
    transformer: Any
    func: Any
    inverse_func: Any
    check_inverse: Any
    def __init__(self, regressor: Any | None = ..., *, transformer: Any | None = ..., func: Any | None = ..., inverse_func: Any | None = ..., check_inverse: bool = ...) -> None: ...
    regressor_: Any
    feature_names_in_: Any
    def fit(self, X, y, **fit_params): ...
    def predict(self, X, **predict_params): ...
    @property
    def n_features_in_(self): ...
