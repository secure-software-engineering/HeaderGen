from ..base import BaseEstimator as BaseEstimator, MetaEstimatorMixin as MetaEstimatorMixin, MultiOutputMixin as MultiOutputMixin, RegressorMixin as RegressorMixin, clone as clone
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils import check_consistent_length as check_consistent_length, check_random_state as check_random_state
from ..utils.random import sample_without_replacement as sample_without_replacement
from ..utils.validation import check_is_fitted as check_is_fitted, has_fit_parameter as has_fit_parameter
from ._base import LinearRegression as LinearRegression
from typing import Any

class RANSACRegressor(MetaEstimatorMixin, RegressorMixin, MultiOutputMixin, BaseEstimator):
    base_estimator: Any
    min_samples: Any
    residual_threshold: Any
    is_data_valid: Any
    is_model_valid: Any
    max_trials: Any
    max_skips: Any
    stop_n_inliers: Any
    stop_score: Any
    stop_probability: Any
    random_state: Any
    loss: Any
    def __init__(self, base_estimator: Any | None = ..., *, min_samples: Any | None = ..., residual_threshold: Any | None = ..., is_data_valid: Any | None = ..., is_model_valid: Any | None = ..., max_trials: int = ..., max_skips=..., stop_n_inliers=..., stop_score=..., stop_probability: float = ..., loss: str = ..., random_state: Any | None = ...) -> None: ...
    n_skips_no_inliers_: int
    n_skips_invalid_data_: int
    n_skips_invalid_model_: int
    n_trials_: int
    estimator_: Any
    inlier_mask_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...
    def predict(self, X): ...
    def score(self, X, y): ...
