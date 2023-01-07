from statsmodels.tools.tools import Bunch as Bunch, add_constant as add_constant
from statsmodels.tsa.arima.params import SARIMAXParams as SARIMAXParams
from statsmodels.tsa.arima.specification import SARIMAXSpecification as SARIMAXSpecification
from statsmodels.tsa.statespace.sarimax import SARIMAX as SARIMAX
from typing import Any

def statespace(endog, exog: Any | None = ..., order=..., seasonal_order=..., include_constant: bool = ..., enforce_stationarity: bool = ..., enforce_invertibility: bool = ..., concentrate_scale: bool = ..., start_params: Any | None = ..., fit_kwargs: Any | None = ...): ...
