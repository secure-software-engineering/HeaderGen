from pandas._typing import Scalar as Scalar
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.util.numba_ import NUMBA_FUNC_CACHE as NUMBA_FUNC_CACHE, get_jit_arguments as get_jit_arguments
from typing import Union, Callable

def generate_shared_aggregator(func: Callable[..., Scalar], engine_kwargs: Union[dict[str, bool], None], cache_key_str: str): ...
