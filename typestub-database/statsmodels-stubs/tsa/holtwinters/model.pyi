import numpy as np
from statsmodels.compat.pandas import deprecate_kwarg as deprecate_kwarg
from statsmodels.tools.validation import array_like as array_like, bool_like as bool_like, dict_like as dict_like, float_like as float_like, int_like as int_like, string_like as string_like
from statsmodels.tsa.base.tsa_model import TimeSeriesModel as TimeSeriesModel
from statsmodels.tsa.holtwinters._exponential_smoothers import HoltWintersArgs as HoltWintersArgs
from statsmodels.tsa.holtwinters._smoothers import to_restricted as to_restricted, to_unrestricted as to_unrestricted
from statsmodels.tsa.holtwinters.results import HoltWintersResults as HoltWintersResults, HoltWintersResultsWrapper as HoltWintersResultsWrapper
from statsmodels.tsa.tsatools import freq_to_period as freq_to_period
from typing import Any

SMOOTHERS: Any
PY_SMOOTHERS: Any

def opt_wrapper(func): ...

class _OptConfig:
    alpha: float
    beta: float
    phi: float
    gamma: float
    level: float
    trend: float
    seasonal: np.ndarray
    y: np.ndarray
    params: np.ndarray
    mask: np.ndarray
    mle_retvals: Any
    def unpack_parameters(self, params) -> _OptConfig: ...

class ExponentialSmoothing(TimeSeriesModel):
    trend: Any
    damped_trend: Any
    seasonal: Any
    has_trend: Any
    has_seasonal: Any
    seasonal_periods: Any
    nobs: Any
    def __init__(self, endog, trend: Any | None = ..., damped_trend: bool = ..., seasonal: Any | None = ..., *, seasonal_periods: Any | None = ..., initialization_method: str = ..., initial_level: Any | None = ..., initial_trend: Any | None = ..., initial_seasonal: Any | None = ..., use_boxcox: bool = ..., bounds: Any | None = ..., dates: Any | None = ..., freq: Any | None = ..., missing: str = ...) -> None: ...
    def fix_params(self, values) -> None: ...
    def predict(self, params, start: Any | None = ..., end: Any | None = ...): ...
    def fit(self, smoothing_level: Any | None = ..., smoothing_trend: Any | None = ..., smoothing_seasonal: Any | None = ..., damping_trend: Any | None = ..., *, optimized: bool = ..., remove_bias: bool = ..., start_params: Any | None = ..., method: Any | None = ..., minimize_kwargs: Any | None = ..., use_brute: bool = ..., use_boxcox: Any | None = ..., use_basinhopping: Any | None = ..., initial_level: Any | None = ..., initial_trend: Any | None = ...): ...
    def initial_values(self, initial_level: Any | None = ..., initial_trend: Any | None = ..., force: bool = ...): ...

class SimpleExpSmoothing(ExponentialSmoothing):
    def __init__(self, endog, initialization_method: Any | None = ..., initial_level: Any | None = ...) -> None: ...
    def fit(self, smoothing_level: Any | None = ..., *, optimized: bool = ..., start_params: Any | None = ..., initial_level: Any | None = ..., use_brute: bool = ..., use_boxcox: Any | None = ..., remove_bias: bool = ..., method: Any | None = ..., minimize_kwargs: Any | None = ...): ...

class Holt(ExponentialSmoothing):
    def __init__(self, endog, exponential: bool = ..., damped_trend: bool = ..., initialization_method: Any | None = ..., initial_level: Any | None = ..., initial_trend: Any | None = ...) -> None: ...
    def fit(self, smoothing_level: Any | None = ..., smoothing_trend: Any | None = ..., *, damping_trend: Any | None = ..., optimized: bool = ..., start_params: Any | None = ..., initial_level: Any | None = ..., initial_trend: Any | None = ..., use_brute: bool = ..., use_boxcox: Any | None = ..., remove_bias: bool = ..., method: Any | None = ..., minimize_kwargs: Any | None = ...): ...
