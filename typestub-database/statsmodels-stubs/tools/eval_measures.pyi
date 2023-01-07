from statsmodels.tools.validation import array_like as array_like

def mse(x1, x2, axis: int = ...): ...
def rmse(x1, x2, axis: int = ...): ...
def rmspe(y, y_hat, axis: int = ..., zeros=...): ...
def maxabs(x1, x2, axis: int = ...): ...
def meanabs(x1, x2, axis: int = ...): ...
def medianabs(x1, x2, axis: int = ...): ...
def bias(x1, x2, axis: int = ...): ...
def medianbias(x1, x2, axis: int = ...): ...
def vare(x1, x2, ddof: int = ..., axis: int = ...): ...
def stde(x1, x2, ddof: int = ..., axis: int = ...): ...
def iqr(x1, x2, axis: int = ...): ...
def aic(llf, nobs, df_modelwc): ...
def aicc(llf, nobs, df_modelwc): ...
def bic(llf, nobs, df_modelwc): ...
def hqic(llf, nobs, df_modelwc): ...
def aic_sigma(sigma2, nobs, df_modelwc, islog: bool = ...): ...
def aicc_sigma(sigma2, nobs, df_modelwc, islog: bool = ...): ...
def bic_sigma(sigma2, nobs, df_modelwc, islog: bool = ...): ...
def hqic_sigma(sigma2, nobs, df_modelwc, islog: bool = ...): ...
