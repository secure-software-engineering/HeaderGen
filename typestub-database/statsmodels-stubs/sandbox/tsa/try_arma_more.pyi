from statsmodels.tsa.arima_process import arma_generate_sample as arma_generate_sample
from statsmodels.tsa.stattools import acovf as acovf
from typing import Any

hastalkbox: bool
ar: Any
ma: Any
n_startup: int
nobs: int
xo: Any
x: Any
rescale: int
w: Any
h: Any
sd: Any
pm: Any
maxind: Any
wmax = w[maxind]
sdmax = sd[maxind]
sdm: Any
wm: Any
sdp: Any
wp: Any
xacov: Any
nr: Any
xacovfft: Any
sdpa: Any
wpa: Any
