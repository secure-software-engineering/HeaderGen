from scipy.stats.distributions import rv_continuous
from typing import Any

class genpareto2_gen(rv_continuous): ...

genpareto2: Any
shape: Any
loc: Any
scale: Any
rv: Any
quant: Any

def paramstopot(thresh, shape, scale): ...
def paramsfrompot(thresh, shape, scalepot): ...
def warnif(cond, msg) -> None: ...
def meanexcess(thresh, shape, scale): ...
def meanexcess_plot(data, params: Any | None = ..., lidx: int = ..., uidx: int = ..., method: str = ..., plot: int = ...): ...

data: Any
tmp: Any

def meanexcess_emp(data): ...
def meanexcess_dist(self, lb, *args, **kwds): ...

ds: Any
me: Any
mc: Any
rvs: Any
