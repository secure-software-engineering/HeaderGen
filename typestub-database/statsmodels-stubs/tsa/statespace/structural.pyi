from .initialization import Initialization as Initialization
from .mlemodel import MLEModel as MLEModel, MLEResults as MLEResults, MLEResultsWrapper as MLEResultsWrapper
from .tools import companion_matrix as companion_matrix, constrain_stationary_univariate as constrain_stationary_univariate, prepare_exog as prepare_exog, unconstrain_stationary_univariate as unconstrain_stationary_univariate
from statsmodels.compat.pandas import Appender as Appender
from statsmodels.tools.sm_exceptions import OutputWarning as OutputWarning, SpecificationWarning as SpecificationWarning
from statsmodels.tools.tools import Bunch as Bunch
from statsmodels.tsa.filters.hp_filter import hpfilter as hpfilter
from statsmodels.tsa.tsatools import lagmat as lagmat
from typing import Any

class UnobservedComponents(MLEModel):
    level: Any
    trend: Any
    seasonal_periods: Any
    seasonal: Any
    freq_seasonal_periods: Any
    freq_seasonal_harmonics: Any
    freq_seasonal: Any
    cycle: Any
    ar_order: Any
    autoregressive: Any
    irregular: Any
    stochastic_level: Any
    stochastic_trend: Any
    stochastic_seasonal: Any
    stochastic_freq_seasonal: Any
    stochastic_cycle: Any
    damped_cycle: Any
    mle_regression: Any
    use_exact_diffuse: Any
    trend_specification: Any
    trend_mask: Any
    regression: Any
    cycle_frequency_bound: Any
    def __init__(self, endog, level: bool = ..., trend: bool = ..., seasonal: Any | None = ..., freq_seasonal: Any | None = ..., cycle: bool = ..., autoregressive: Any | None = ..., exog: Any | None = ..., irregular: bool = ..., stochastic_level: bool = ..., stochastic_trend: bool = ..., stochastic_seasonal: bool = ..., stochastic_freq_seasonal: Any | None = ..., stochastic_cycle: bool = ..., damped_cycle: bool = ..., cycle_period_bounds: Any | None = ..., mle_regression: bool = ..., use_exact_diffuse: bool = ..., **kwargs) -> None: ...
    parameters: Any
    parameters_obs_intercept: Any
    parameters_obs_cov: Any
    parameters_transition: Any
    parameters_state_cov: Any
    k_obs_intercept: Any
    k_obs_cov: Any
    k_transition: Any
    k_state_cov: Any
    k_params: Any
    def setup(self) -> None: ...
    loglikelihood_burn: Any
    def initialize_default(self, approximate_diffuse_variance: Any | None = ...) -> None: ...
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

class UnobservedComponentsResults(MLEResults):
    df_resid: Any
    specification: Any
    def __init__(self, model, params, filter_results, cov_type: Any | None = ..., **kwargs) -> None: ...
    @property
    def level(self): ...
    @property
    def trend(self): ...
    @property
    def seasonal(self): ...
    @property
    def freq_seasonal(self): ...
    @property
    def cycle(self): ...
    @property
    def autoregressive(self): ...
    @property
    def regression_coefficients(self): ...
    def plot_components(self, which: Any | None = ..., alpha: float = ..., observed: bool = ..., level: bool = ..., trend: bool = ..., seasonal: bool = ..., freq_seasonal: bool = ..., cycle: bool = ..., autoregressive: bool = ..., legend_loc: str = ..., fig: Any | None = ..., figsize: Any | None = ...): ...
    def summary(self, alpha: float = ..., start: Any | None = ...): ...

class UnobservedComponentsResultsWrapper(MLEResultsWrapper): ...
