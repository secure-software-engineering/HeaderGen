from . import tools as tools
from .representation import FrozenRepresentation as FrozenRepresentation, OptionWrapper as OptionWrapper, Representation as Representation
from .tools import reorder_missing_matrix as reorder_missing_matrix, reorder_missing_vector as reorder_missing_vector
from statsmodels.tools.sm_exceptions import ValueWarning as ValueWarning
from typing import Any

FILTER_CONVENTIONAL: int
FILTER_EXACT_INITIAL: int
FILTER_AUGMENTED: int
FILTER_SQUARE_ROOT: int
FILTER_UNIVARIATE: int
FILTER_COLLAPSED: int
FILTER_EXTENDED: int
FILTER_UNSCENTED: int
FILTER_CONCENTRATED: int
FILTER_CHANDRASEKHAR: int
INVERT_UNIVARIATE: int
SOLVE_LU: int
INVERT_LU: int
SOLVE_CHOLESKY: int
INVERT_CHOLESKY: int
STABILITY_FORCE_SYMMETRY: int
MEMORY_STORE_ALL: int
MEMORY_NO_FORECAST_MEAN: int
MEMORY_NO_FORECAST_COV: int
MEMORY_NO_FORECAST: Any
MEMORY_NO_PREDICTED_MEAN: int
MEMORY_NO_PREDICTED_COV: int
MEMORY_NO_PREDICTED: Any
MEMORY_NO_FILTERED_MEAN: int
MEMORY_NO_FILTERED_COV: int
MEMORY_NO_FILTERED: Any
MEMORY_NO_LIKELIHOOD: int
MEMORY_NO_GAIN: int
MEMORY_NO_SMOOTHING: int
MEMORY_NO_STD_FORECAST: int
MEMORY_CONSERVE: Any
TIMING_INIT_PREDICTED: int
TIMING_INIT_FILTERED: int

class KalmanFilter(Representation):
    filter_methods: Any
    filter_conventional: Any
    filter_exact_initial: Any
    filter_augmented: Any
    filter_square_root: Any
    filter_univariate: Any
    filter_collapsed: Any
    filter_extended: Any
    filter_unscented: Any
    filter_concentrated: Any
    filter_chandrasekhar: Any
    inversion_methods: Any
    invert_univariate: Any
    solve_lu: Any
    invert_lu: Any
    solve_cholesky: Any
    invert_cholesky: Any
    stability_methods: Any
    stability_force_symmetry: Any
    memory_options: Any
    memory_store_all: Any
    memory_no_forecast_mean: Any
    memory_no_forecast_cov: Any
    @property
    def memory_no_forecast(self): ...
    @memory_no_forecast.setter
    def memory_no_forecast(self, value) -> None: ...
    memory_no_predicted_mean: Any
    memory_no_predicted_cov: Any
    @property
    def memory_no_predicted(self): ...
    @memory_no_predicted.setter
    def memory_no_predicted(self, value) -> None: ...
    memory_no_filtered_mean: Any
    memory_no_filtered_cov: Any
    @property
    def memory_no_filtered(self): ...
    @memory_no_filtered.setter
    def memory_no_filtered(self, value) -> None: ...
    memory_no_likelihood: Any
    memory_no_gain: Any
    memory_no_smoothing: Any
    memory_no_std_forecast: Any
    memory_conserve: Any
    timing_options: Any
    timing_init_predicted: Any
    timing_init_filtered: Any
    filter_method: Any
    inversion_method: Any
    stability_method: Any
    conserve_memory: Any
    filter_timing: Any
    loglikelihood_burn: Any
    results_class: Any
    prefix_kalman_filter_map: Any
    tolerance: Any
    def __init__(self, k_endog, k_states, k_posdef: Any | None = ..., loglikelihood_burn: int = ..., tolerance: float = ..., results_class: Any | None = ..., kalman_filter_classes: Any | None = ..., **kwargs) -> None: ...
    def set_filter_method(self, filter_method: Any | None = ..., **kwargs) -> None: ...
    def set_inversion_method(self, inversion_method: Any | None = ..., **kwargs) -> None: ...
    def set_stability_method(self, stability_method: Any | None = ..., **kwargs) -> None: ...
    def set_conserve_memory(self, conserve_memory: Any | None = ..., **kwargs) -> None: ...
    def set_filter_timing(self, alternate_timing: Any | None = ..., **kwargs) -> None: ...
    def fixed_scale(self, scale) -> None: ...
    def filter(self, filter_method: Any | None = ..., inversion_method: Any | None = ..., stability_method: Any | None = ..., conserve_memory: Any | None = ..., filter_timing: Any | None = ..., tolerance: Any | None = ..., loglikelihood_burn: Any | None = ..., complex_step: bool = ...): ...
    def loglike(self, **kwargs): ...
    def loglikeobs(self, **kwargs): ...
    def simulate(self, nsimulations, measurement_shocks: Any | None = ..., state_shocks: Any | None = ..., initial_state: Any | None = ...): ...
    def impulse_responses(self, steps: int = ..., impulse: int = ..., orthogonalized: bool = ..., cumulative: bool = ..., direct: bool = ...): ...

class FilterResults(FrozenRepresentation):
    def __init__(self, model) -> None: ...
    def update_representation(self, model, only_options: bool = ...) -> None: ...
    initial_state: Any
    initial_state_cov: Any
    filter_method: Any
    inversion_method: Any
    stability_method: Any
    conserve_memory: Any
    filter_timing: Any
    tolerance: Any
    loglikelihood_burn: Any
    converged: Any
    period_converged: Any
    filtered_state: Any
    filtered_state_cov: Any
    predicted_state: Any
    predicted_state_cov: Any
    tmp1: Any
    tmp2: Any
    tmp3: Any
    tmp4: Any
    M: Any
    M_diffuse: Any
    forecasts: Any
    forecasts_error: Any
    forecasts_error_cov: Any
    llf_obs: Any
    nobs_diffuse: Any
    initial_diffuse_state_cov: Any
    forecasts_error_diffuse_cov: Any
    predicted_diffuse_state_cov: Any
    missing_forecasts: Any
    missing_forecasts_error: Any
    missing_forecasts_error_cov: Any
    collapsed_forecasts: Any
    collapsed_forecasts_error: Any
    collapsed_forecasts_error_cov: Any
    scale: float
    obs_cov: Any
    state_cov: Any
    filter_concentrated: bool
    llf: Any
    def update_filter(self, kalman_filter) -> None: ...
    @property
    def kalman_gain(self): ...
    @property
    def standardized_forecasts_error(self): ...
    def predict(self, start: Any | None = ..., end: Any | None = ..., dynamic: Any | None = ..., **kwargs): ...

class PredictionResults(FilterResults):
    representation_attributes: Any
    filter_attributes: Any
    results: Any
    npredictions: Any
    start: Any
    end: Any
    nstatic: Any
    ndynamic: Any
    nforecast: Any
    def __init__(self, results, start, end, nstatic, ndynamic, nforecast) -> None: ...
    def clear(self) -> None: ...
    def __getattr__(self, attr): ...
