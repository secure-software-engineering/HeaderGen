import scipy.stats
from .._config import config_context as config_context, get_config as get_config
from ..externals._lobpcg import lobpcg as lobpcg
from scipy.optimize.linesearch import line_search_wolfe1 as line_search_wolfe1, line_search_wolfe2 as line_search_wolfe2
from typing import Any

np_version: Any
sp_version: Any

class loguniform(scipy.stats.reciprocal): ...

def delayed(function): ...

class _FuncWrapper:
    function: Any
    config: Any
    def __init__(self, function) -> None: ...
    def __call__(self, *args, **kwargs): ...

def linspace(start, stop, num: int = ..., endpoint: bool = ..., retstep: bool = ..., dtype: Any | None = ..., axis: int = ...): ...

percentile: Any

def threadpool_limits(limits: Any | None = ..., user_api: Any | None = ...): ...
def threadpool_info(): ...
