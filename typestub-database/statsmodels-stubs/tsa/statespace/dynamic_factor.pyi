from .mlemodel import MLEModel as MLEModel, MLEResults as MLEResults, MLEResultsWrapper as MLEResultsWrapper
from .tools import constrain_stationary_multivariate as constrain_stationary_multivariate, constrain_stationary_univariate as constrain_stationary_univariate, is_invertible as is_invertible, prepare_exog as prepare_exog, unconstrain_stationary_multivariate as unconstrain_stationary_multivariate, unconstrain_stationary_univariate as unconstrain_stationary_univariate
from statsmodels.compat.pandas import Appender as Appender
from statsmodels.multivariate.pca import PCA as PCA
from statsmodels.regression.linear_model import OLS as OLS
from statsmodels.tools.decorators import cache_readonly as cache_readonly
from statsmodels.tools.tools import Bunch as Bunch
from statsmodels.tsa.arima.model import ARIMA as ARIMA
from statsmodels.tsa.tsatools import lagmat as lagmat
from statsmodels.tsa.vector_ar.var_model import VAR as VAR
from typing import Any

class DynamicFactor(MLEModel):
    enforce_stationarity: Any
    k_factors: Any
    factor_order: Any
    error_order: Any
    error_var: Any
    error_cov_type: Any
    mle_regression: Any
    parameters: Any
    k_params: Any
    def __init__(self, endog, k_factors, factor_order, exog: Any | None = ..., error_order: int = ..., error_var: bool = ..., error_cov_type: str = ..., enforce_stationarity: bool = ..., **kwargs): ...
    def clone(self, endog, exog: Any | None = ..., **kwargs): ...
    @property
    def start_params(self): ...
    @property
    def param_names(self): ...
    @property
    def state_names(self): ...
    def transform_params(self, unconstrained): ...
    def untransform_params(self, constrained): ...
    def update(self, params, transformed: bool = ..., includes_fixed: bool = ..., complex_step: bool = ...) -> None: ...

class DynamicFactorResults(MLEResults):
    df_resid: Any
    specification: Any
    coefficient_matrices_var: Any
    coefficient_matrices_error: Any
    def __init__(self, model, params, filter_results, cov_type: Any | None = ..., **kwargs) -> None: ...
    @property
    def factors(self): ...
    def coefficients_of_determination(self): ...
    def plot_coefficients_of_determination(self, endog_labels: Any | None = ..., fig: Any | None = ..., figsize: Any | None = ...): ...
    def summary(self, alpha: float = ..., start: Any | None = ..., separate_params: bool = ...): ...

class DynamicFactorResultsWrapper(MLEResultsWrapper): ...
