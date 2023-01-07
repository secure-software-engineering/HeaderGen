from statsmodels.compat.pandas import deprecate_kwarg as deprecate_kwarg
from statsmodels.tools.tools import Bunch as Bunch
from statsmodels.tsa.arima.params import SARIMAXParams as SARIMAXParams
from statsmodels.tsa.arima.specification import SARIMAXSpecification as SARIMAXSpecification
from statsmodels.tsa.stattools import acovf as acovf

def durbin_levinson(endog, ar_order: int = ..., demean: bool = ..., adjusted: bool = ...): ...
