import numpy as np
from pandas._libs.sparse import IntIndex as IntIndex
from pandas._typing import Dtype as Dtype, npt as npt
from pandas.core.arrays import ExtensionArray as ExtensionArray, SparseArray as SparseArray
from pandas.core.arrays.categorical import factorize_from_iterable as factorize_from_iterable
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike
from pandas.core.dtypes.cast import maybe_promote as maybe_promote
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int, is_1d_only_ea_dtype as is_1d_only_ea_dtype, is_extension_array_dtype as is_extension_array_dtype, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_object_dtype as is_object_dtype, needs_i8_conversion as needs_i8_conversion
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.missing import notna as notna
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.indexes.api import Index as Index, MultiIndex as MultiIndex
from pandas.core.indexes.frozen import FrozenList as FrozenList
from pandas.core.series import Series as Series
from pandas.core.sorting import compress_group_index as compress_group_index, decons_obs_group_ids as decons_obs_group_ids, get_compressed_ids as get_compressed_ids, get_group_index as get_group_index, get_group_index_sorter as get_group_index_sorter
from pandas.errors import PerformanceWarning as PerformanceWarning
from pandas.util._decorators import cache_readonly as cache_readonly
from typing import Union, Any

class _Unstacker:
    constructor: Any
    index: Any
    level: Any
    lift: Any
    new_index_levels: Any
    new_index_names: Any
    removed_name: Any
    removed_level: Any
    removed_level_full: Any
    def __init__(self, index: MultiIndex, level: int = ..., constructor: Any | None = ...) -> None: ...
    def sorted_labels(self): ...
    def mask_all(self) -> bool: ...
    def arange_result(self) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.bool_]]: ...
    def get_result(self, values, value_columns, fill_value): ...
    def get_new_values(self, values, fill_value: Any | None = ...): ...
    def get_new_columns(self, value_columns: Union[Index, None]): ...
    def new_index(self): ...

def unstack(obj, level, fill_value: Any | None = ...): ...
def stack(frame, level: int = ..., dropna: bool = ...): ...
def stack_multiple(frame, level, dropna: bool = ...): ...
def get_dummies(data, prefix: Any | None = ..., prefix_sep: str = ..., dummy_na: bool = ..., columns: Any | None = ..., sparse: bool = ..., drop_first: bool = ..., dtype: Union[Dtype, None] = ...) -> DataFrame: ...
