from statsmodels.tsa.statespace import tools as tools
from statsmodels.tsa.statespace.kalman_filter import FilterResults as FilterResults, KalmanFilter as KalmanFilter
from statsmodels.tsa.statespace.representation import OptionWrapper as OptionWrapper
from statsmodels.tsa.statespace.tools import copy_index_matrix as copy_index_matrix, reorder_missing_matrix as reorder_missing_matrix, reorder_missing_vector as reorder_missing_vector
from typing import Any

SMOOTHER_STATE: int
SMOOTHER_STATE_COV: int
SMOOTHER_DISTURBANCE: int
SMOOTHER_DISTURBANCE_COV: int
SMOOTHER_STATE_AUTOCOV: int
SMOOTHER_ALL: Any
SMOOTH_CONVENTIONAL: int
SMOOTH_CLASSICAL: int
SMOOTH_ALTERNATIVE: int
SMOOTH_UNIVARIATE: int

class KalmanSmoother(KalmanFilter):
    smoother_outputs: Any
    smoother_state: Any
    smoother_state_cov: Any
    smoother_disturbance: Any
    smoother_disturbance_cov: Any
    smoother_state_autocov: Any
    smoother_all: Any
    smooth_methods: Any
    smooth_conventional: Any
    smooth_alternative: Any
    smooth_classical: Any
    smooth_univariate: Any
    smoother_output: Any
    smooth_method: int
    prefix_kalman_smoother_map: Any
    def __init__(self, k_endog, k_states, k_posdef: Any | None = ..., results_class: Any | None = ..., kalman_smoother_classes: Any | None = ..., **kwargs) -> None: ...
    def set_smoother_output(self, smoother_output: Any | None = ..., **kwargs) -> None: ...
    def set_smooth_method(self, smooth_method: Any | None = ..., **kwargs) -> None: ...
    def smooth(self, smoother_output: Any | None = ..., smooth_method: Any | None = ..., results: Any | None = ..., run_filter: bool = ..., prefix: Any | None = ..., complex_step: bool = ..., update_representation: bool = ..., update_filter: bool = ..., update_smoother: bool = ..., **kwargs): ...

class SmootherResults(FilterResults):
    def update_representation(self, model, only_options: bool = ...) -> None: ...
    innovations_transition: Any
    scaled_smoothed_diffuse_estimator: Any
    scaled_smoothed_diffuse1_estimator_cov: Any
    scaled_smoothed_diffuse2_estimator_cov: Any
    scaled_smoothed_estimator: Any
    scaled_smoothed_estimator_cov: Any
    def update_smoother(self, smoother) -> None: ...
    def smoothed_state_autocovariance(self, lag: int = ..., t: Any | None = ..., start: Any | None = ..., end: Any | None = ..., extend_kwargs: Any | None = ...): ...
    def news(self, previous, t: Any | None = ..., start: Any | None = ..., end: Any | None = ..., revised: Any | None = ..., design: Any | None = ...): ...
    def smoothed_state_gain(self, updates_ix, t: Any | None = ..., start: Any | None = ..., end: Any | None = ..., extend_kwargs: Any | None = ...): ...
    @property
    def smoothed_forecasts(self): ...
    @property
    def smoothed_forecasts_error(self): ...
    @property
    def smoothed_forecasts_error_cov(self): ...
