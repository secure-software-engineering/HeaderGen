from statsmodels.compat.pandas import Appender as Appender
from statsmodels.tsa.arima.estimators.burg import burg as burg
from statsmodels.tsa.arima.estimators.hannan_rissanen import hannan_rissanen as hannan_rissanen
from statsmodels.tsa.arima.estimators.innovations import innovations as innovations, innovations_mle as innovations_mle
from statsmodels.tsa.arima.estimators.yule_walker import yule_walker as yule_walker
from statsmodels.tsa.arima.specification import SARIMAXSpecification as SARIMAXSpecification
from statsmodels.tsa.statespace import sarimax as sarimax
from statsmodels.tsa.statespace.kalman_filter import MEMORY_CONSERVE as MEMORY_CONSERVE
from statsmodels.tsa.statespace.tools import diff as diff
from typing import Any

class ARIMA(sarimax.SARIMAX):
    trend: Any
    k_exog: Any
    k_trend: Any
    def __init__(self, endog, exog: Any | None = ..., order=..., seasonal_order=..., trend: Any | None = ..., enforce_stationarity: bool = ..., enforce_invertibility: bool = ..., concentrate_scale: bool = ..., trend_offset: int = ..., dates: Any | None = ..., freq: Any | None = ..., missing: str = ..., validate_specification: bool = ...) -> None: ...
    def fit(self, start_params: Any | None = ..., transformed: bool = ..., includes_fixed: bool = ..., method: Any | None = ..., method_kwargs: Any | None = ..., gls: Any | None = ..., gls_kwargs: Any | None = ..., cov_type: Any | None = ..., cov_kwds: Any | None = ..., return_params: bool = ..., low_memory: bool = ...): ...

class ARIMAResults(sarimax.SARIMAXResults):
    def append(self, endog, exog: Any | None = ..., refit: bool = ..., fit_kwargs: Any | None = ..., **kwargs): ...

class ARIMAResultsWrapper(sarimax.SARIMAXResultsWrapper): ...
