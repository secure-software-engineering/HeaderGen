from statsmodels.compat.python import lrange as lrange
from statsmodels.sandbox.tools.mctools import StatTestMC as StatTestMC
from statsmodels.stats.diagnostic import acorr_ljungbox as acorr_ljungbox
from statsmodels.tsa.stattools import adfuller as adfuller
from typing import Any

def normalnoisesim(nobs: int = ..., loc: float = ...): ...
def lb(x): ...

mc1: Any
frac: Any
crit: Any

def randwalksim(nobs: int = ..., drift: float = ...): ...
def adf20(x): ...

mc2: Any
doplot: int
