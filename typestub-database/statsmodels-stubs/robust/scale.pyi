from . import norms as norms
from statsmodels.tools import tools as tools
from statsmodels.tools.validation import array_like as array_like, float_like as float_like
from typing import Any

def mad(a, c=..., axis: int = ..., center=...): ...
def iqr(a, c=..., axis: int = ...): ...
def qn_scale(a, c=..., axis: int = ...): ...

class Huber:
    c: Any
    maxiter: Any
    tol: Any
    norm: Any
    gamma: Any
    def __init__(self, c: float = ..., tol: float = ..., maxiter: int = ..., norm: Any | None = ...) -> None: ...
    def __call__(self, a, mu: Any | None = ..., initscale: Any | None = ..., axis: int = ...): ...

huber: Any

class HuberScale:
    d: Any
    tol: Any
    maxiter: Any
    def __init__(self, d: float = ..., tol: float = ..., maxiter: int = ...) -> None: ...
    def __call__(self, df_resid, nobs, resid): ...

hubers_scale: Any
