from .initialization import Initialization as Initialization
from .kalman_filter import INVERT_UNIVARIATE as INVERT_UNIVARIATE, SOLVE_LU as SOLVE_LU
from .mlemodel import MLEModel as MLEModel, MLEResults as MLEResults, MLEResultsWrapper as MLEResultsWrapper
from .tools import concat as concat, constrain_stationary_multivariate as constrain_stationary_multivariate, is_invertible as is_invertible, prepare_exog as prepare_exog, prepare_trend_data as prepare_trend_data, prepare_trend_spec as prepare_trend_spec, unconstrain_stationary_multivariate as unconstrain_stationary_multivariate
from statsmodels.compat.pandas import Appender as Appender
from statsmodels.tools.sm_exceptions import EstimationWarning as EstimationWarning
from statsmodels.tools.tools import Bunch as Bunch
from statsmodels.tsa.vector_ar import var_model as var_model
from typing import Any

class VARMAX(MLEModel):
    error_cov_type: Any
    measurement_error: Any
    enforce_stationarity: Any
    enforce_invertibility: Any
    order: Any
    k_ar: Any
    k_ma: Any
    trend: Any
    trend_offset: Any
    mle_regression: Any
    parameters: Any
    k_params: Any
    def __init__(self, endog, exog: Any | None = ..., order=..., trend: str = ..., error_cov_type: str = ..., measurement_error: bool = ..., enforce_stationarity: bool = ..., enforce_invertibility: bool = ..., trend_offset: int = ..., **kwargs): ...
    def clone(self, endog, exog: Any | None = ..., **kwargs): ...
    @property
    def start_params(self): ...
    @property
    def param_names(self): ...
    def transform_params(self, unconstrained): ...
    def untransform_params(self, constrained): ...
    def update(self, params, transformed: bool = ..., includes_fixed: bool = ..., complex_step: bool = ...) -> None: ...
    def simulate(self, params, nsimulations, measurement_shocks: Any | None = ..., state_shocks: Any | None = ..., initial_state: Any | None = ..., anchor: Any | None = ..., repetitions: Any | None = ..., exog: Any | None = ..., extend_model: Any | None = ..., extend_kwargs: Any | None = ..., transformed: bool = ..., includes_fixed: bool = ..., **kwargs): ...

class VARMAXResults(MLEResults):
    specification: Any
    coefficient_matrices_var: Any
    coefficient_matrices_vma: Any
    def __init__(self, model, params, filter_results, cov_type: Any | None = ..., cov_kwds: Any | None = ..., **kwargs) -> None: ...
    def extend(self, endog, exog: Any | None = ..., **kwargs): ...
    def get_prediction(self, start: Any | None = ..., end: Any | None = ..., dynamic: bool = ..., index: Any | None = ..., exog: Any | None = ..., **kwargs): ...
    def simulate(self, nsimulations, measurement_shocks: Any | None = ..., state_shocks: Any | None = ..., initial_state: Any | None = ..., anchor: Any | None = ..., repetitions: Any | None = ..., exog: Any | None = ..., extend_model: Any | None = ..., extend_kwargs: Any | None = ..., **kwargs): ...
    def summary(self, alpha: float = ..., start: Any | None = ..., separate_params: bool = ...): ...

class VARMAXResultsWrapper(MLEResultsWrapper): ...
