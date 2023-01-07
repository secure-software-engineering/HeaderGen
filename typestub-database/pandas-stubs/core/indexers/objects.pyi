import numpy as np
from pandas._libs.window.indexers import calculate_variable_window_bounds as calculate_variable_window_bounds
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int
from pandas.tseries.offsets import Nano as Nano
from pandas.util._decorators import Appender as Appender
from typing import Union, Any

get_window_bounds_doc: str

class BaseIndexer:
    index_array: Any
    window_size: Any
    def __init__(self, index_array: Union[np.ndarray, None] = ..., window_size: int = ..., **kwargs) -> None: ...
    def get_window_bounds(self, num_values: int = ..., min_periods: Union[int, None] = ..., center: Union[bool, None] = ..., closed: Union[str, None] = ...) -> tuple[np.ndarray, np.ndarray]: ...

class FixedWindowIndexer(BaseIndexer):
    def get_window_bounds(self, num_values: int = ..., min_periods: Union[int, None] = ..., center: Union[bool, None] = ..., closed: Union[str, None] = ...) -> tuple[np.ndarray, np.ndarray]: ...

class VariableWindowIndexer(BaseIndexer):
    def get_window_bounds(self, num_values: int = ..., min_periods: Union[int, None] = ..., center: Union[bool, None] = ..., closed: Union[str, None] = ...) -> tuple[np.ndarray, np.ndarray]: ...

class VariableOffsetWindowIndexer(BaseIndexer):
    index: Any
    offset: Any
    def __init__(self, index_array: Union[np.ndarray, None] = ..., window_size: int = ..., index: Any | None = ..., offset: Any | None = ..., **kwargs) -> None: ...
    def get_window_bounds(self, num_values: int = ..., min_periods: Union[int, None] = ..., center: Union[bool, None] = ..., closed: Union[str, None] = ...) -> tuple[np.ndarray, np.ndarray]: ...

class ExpandingIndexer(BaseIndexer):
    def get_window_bounds(self, num_values: int = ..., min_periods: Union[int, None] = ..., center: Union[bool, None] = ..., closed: Union[str, None] = ...) -> tuple[np.ndarray, np.ndarray]: ...

class FixedForwardWindowIndexer(BaseIndexer):
    def get_window_bounds(self, num_values: int = ..., min_periods: Union[int, None] = ..., center: Union[bool, None] = ..., closed: Union[str, None] = ...) -> tuple[np.ndarray, np.ndarray]: ...

class GroupbyIndexer(BaseIndexer):
    groupby_indices: Any
    window_indexer: Any
    indexer_kwargs: Any
    def __init__(self, index_array: Union[np.ndarray, None] = ..., window_size: Union[int, BaseIndexer] = ..., groupby_indices: Union[dict, None] = ..., window_indexer: type[BaseIndexer] = ..., indexer_kwargs: Union[dict, None] = ..., **kwargs) -> None: ...
    def get_window_bounds(self, num_values: int = ..., min_periods: Union[int, None] = ..., center: Union[bool, None] = ..., closed: Union[str, None] = ...) -> tuple[np.ndarray, np.ndarray]: ...

class ExponentialMovingWindowIndexer(BaseIndexer):
    def get_window_bounds(self, num_values: int = ..., min_periods: Union[int, None] = ..., center: Union[bool, None] = ..., closed: Union[str, None] = ...) -> tuple[np.ndarray, np.ndarray]: ...
