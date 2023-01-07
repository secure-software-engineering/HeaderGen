from statsmodels.tools.tools import Bunch as Bunch
from statsmodels.tsa.arima.estimators.hannan_rissanen import hannan_rissanen as hannan_rissanen
from statsmodels.tsa.arima.params import SARIMAXParams as SARIMAXParams
from statsmodels.tsa.arima.specification import SARIMAXSpecification as SARIMAXSpecification
from statsmodels.tsa.innovations import arma_innovations as arma_innovations
from statsmodels.tsa.statespace.tools import diff as diff
from statsmodels.tsa.stattools import acovf as acovf, innovations_algo as innovations_algo
from typing import Any

def innovations(endog, ma_order: int = ..., demean: bool = ...): ...
def innovations_mle(endog, order=..., seasonal_order=..., demean: bool = ..., enforce_invertibility: bool = ..., start_params: Any | None = ..., minimize_kwargs: Any | None = ...): ...
