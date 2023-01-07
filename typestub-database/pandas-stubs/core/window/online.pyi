from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.util.numba_ import NUMBA_FUNC_CACHE as NUMBA_FUNC_CACHE, get_jit_arguments as get_jit_arguments
from typing import Union, Any, Dict, Optional

def generate_online_numba_ewma_func(engine_kwargs: Optional[Dict[str, bool]]): ...

class EWMMeanState:
    axis: Any
    shape: Any
    adjust: Any
    ignore_na: Any
    new_wt: Any
    old_wt_factor: Any
    old_wt: Any
    last_ewm: Any
    def __init__(self, com, adjust, ignore_na, axis, shape) -> None: ...
    def run_ewm(self, weighted_avg, deltas, min_periods, ewm_func): ...
    def reset(self) -> None: ...
