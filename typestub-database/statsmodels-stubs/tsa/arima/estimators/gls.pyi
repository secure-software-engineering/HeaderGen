from statsmodels.regression.linear_model import OLS as OLS
from statsmodels.tools.tools import Bunch as Bunch, add_constant as add_constant
from statsmodels.tsa.arima.estimators.burg import burg as burg
from statsmodels.tsa.arima.estimators.hannan_rissanen import hannan_rissanen as hannan_rissanen
from statsmodels.tsa.arima.estimators.innovations import innovations as innovations, innovations_mle as innovations_mle
from statsmodels.tsa.arima.estimators.statespace import statespace as statespace
from statsmodels.tsa.arima.estimators.yule_walker import yule_walker as yule_walker
from statsmodels.tsa.arima.params import SARIMAXParams as SARIMAXParams
from statsmodels.tsa.arima.specification import SARIMAXSpecification as SARIMAXSpecification
from statsmodels.tsa.innovations import arma_innovations as arma_innovations
from statsmodels.tsa.statespace.tools import diff as diff
from typing import Any

def gls(endog, exog: Any | None = ..., order=..., seasonal_order=..., include_constant: Any | None = ..., n_iter: Any | None = ..., max_iter: int = ..., tolerance: float = ..., arma_estimator: str = ..., arma_estimator_kwargs: Any | None = ...): ...
