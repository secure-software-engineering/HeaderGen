from statsmodels.regression.linear_model import OLS as OLS, yule_walker as yule_walker
from statsmodels.tools.tools import Bunch as Bunch
from statsmodels.tsa.arima.params import SARIMAXParams as SARIMAXParams
from statsmodels.tsa.arima.specification import SARIMAXSpecification as SARIMAXSpecification
from statsmodels.tsa.tsatools import lagmat as lagmat
from typing import Any

def hannan_rissanen(endog, ar_order: int = ..., ma_order: int = ..., demean: bool = ..., initial_ar_order: Any | None = ..., unbiased: Any | None = ..., fixed_params: Any | None = ...): ...
