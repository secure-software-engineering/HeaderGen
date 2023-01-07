from statsmodels.regression import linear_model as linear_model
from statsmodels.tools.tools import Bunch as Bunch
from statsmodels.tsa.arima.params import SARIMAXParams as SARIMAXParams
from statsmodels.tsa.arima.specification import SARIMAXSpecification as SARIMAXSpecification

def burg(endog, ar_order: int = ..., demean: bool = ...): ...
