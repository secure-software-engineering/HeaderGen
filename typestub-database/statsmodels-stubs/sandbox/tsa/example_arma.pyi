from statsmodels import regression as regression
from statsmodels.graphics.tsaplots import plot_acf as plot_acf
from statsmodels.tsa.arima.model import ARIMA as ARIMA
from statsmodels.tsa.arima_process import arma_acf as arma_acf, arma_acovf as arma_acovf, arma_generate_sample as arma_generate_sample, arma_impulse_response as arma_impulse_response
from statsmodels.tsa.stattools import acf as acf, acovf as acovf
from typing import Any

ar: Any
ma: Any
mod: str
x: Any
x_acf: Any
x_ir: Any

def detrend(x, key: Any | None = ...): ...
def demean(x, axis: int = ...): ...
def detrend_mean(x): ...
def detrend_none(x): ...
def detrend_linear(y): ...
def acovf_explicit(ar, ma, nobs): ...
def acovf_arma11(ar, ma): ...
def acovf_ma2(ma): ...
def acovf_ma1(ma): ...

ar1: Any
ar0: Any
ma1: Any
ma2: Any
ma0: Any
comparefn: Any
cases: Any
myacovf: Any
myacf: Any
othacovf: Any

def ar_generator(N: int = ..., sigma: float = ...): ...
def autocorr(s, axis: int = ...): ...
def norm_corr(x, y, mode: str = ...): ...
def pltacorr(self, x, **kwargs): ...
def pltxcorr(self, x, y, normed: bool = ..., detrend=..., usevlines: bool = ..., maxlags: int = ..., **kwargs): ...

arrvs: Any
arma: Any
res: Any
acf1: Any
acovf1b: Any
acf2: Any
acf2m: Any
ax: Any
