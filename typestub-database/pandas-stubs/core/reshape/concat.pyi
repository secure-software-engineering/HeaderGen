from pandas.core.frame import DataFrame as DataFrame, Series as Series
from pandas._typing import Axis as Axis
from pandas.core.arrays.categorical import factorize_from_iterable as factorize_from_iterable, factorize_from_iterables as factorize_from_iterables
from pandas.core.dtypes.concat import concat_compat as concat_compat
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.dtypes.inference import is_bool as is_bool
from pandas.core.dtypes.missing import isna as isna
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.indexes.api import Index as Index, MultiIndex as MultiIndex, all_indexes_same as all_indexes_same, default_index as default_index, ensure_index as ensure_index, get_objs_combined_axis as get_objs_combined_axis, get_unanimous_names as get_unanimous_names
from pandas.core.internals import concatenate_managers as concatenate_managers
from pandas.util._decorators import cache_readonly as cache_readonly, deprecate_nonkeyword_arguments as deprecate_nonkeyword_arguments
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Union, Any, Hashable, Iterable, Literal, Mapping, overload

@overload
def concat(objs: Union[Iterable[DataFrame], Mapping[Hashable, DataFrame]], axis: Literal[0, index] = ..., join: str = ..., ignore_index: bool = ..., keys=..., levels=..., names=..., verify_integrity: bool = ..., sort: bool = ..., copy: bool = ...) -> DataFrame: ...
@overload
def concat(objs: Union[Iterable[Series], Mapping[Hashable, Series]], axis: Literal[0, index] = ..., join: str = ..., ignore_index: bool = ..., keys=..., levels=..., names=..., verify_integrity: bool = ..., sort: bool = ..., copy: bool = ...) -> Series: ...
@overload
def concat(objs: Union[Iterable[NDFrame], Mapping[Hashable, NDFrame]], axis: Literal[0, index] = ..., join: str = ..., ignore_index: bool = ..., keys=..., levels=..., names=..., verify_integrity: bool = ..., sort: bool = ..., copy: bool = ...) -> Union[DataFrame, Series]: ...
@overload
def concat(objs: Union[Iterable[NDFrame], Mapping[Hashable, NDFrame]], axis: Literal[1, columns], join: str = ..., ignore_index: bool = ..., keys=..., levels=..., names=..., verify_integrity: bool = ..., sort: bool = ..., copy: bool = ...) -> DataFrame: ...
@overload
def concat(objs: Union[Iterable[NDFrame], Mapping[Hashable, NDFrame]], axis: Axis = ..., join: str = ..., ignore_index: bool = ..., keys=..., levels=..., names=..., verify_integrity: bool = ..., sort: bool = ..., copy: bool = ...) -> Union[DataFrame, Series]: ...

class _Concatenator:
    intersect: bool
    objs: Any
    bm_axis: Any
    axis: Any
    keys: Any
    names: Any
    levels: Any
    sort: Any
    ignore_index: Any
    verify_integrity: Any
    copy: Any
    new_axes: Any
    def __init__(self, objs: Union[Iterable[NDFrame], Mapping[Hashable, NDFrame]], axis: int = ..., join: str = ..., keys: Any | None = ..., levels: Any | None = ..., names: Any | None = ..., ignore_index: bool = ..., verify_integrity: bool = ..., copy: bool = ..., sort: bool = ...) -> None: ...
    def get_result(self): ...
