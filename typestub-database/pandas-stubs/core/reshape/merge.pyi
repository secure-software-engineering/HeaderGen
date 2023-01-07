import numpy as np
from pandas import (
    Categorical as Categorical,
    Index as Index,
    MultiIndex as MultiIndex,
    Series as Series,
)
from pandas.core.frame import DataFrame as DataFrame
from pandas._libs import Timedelta as Timedelta, lib as lib
from pandas._typing import (
    ArrayLike as ArrayLike,
    DtypeObj as DtypeObj,
    IndexLabel as IndexLabel,
    Suffixes as Suffixes,
    npt as npt,
)
from pandas.core import groupby as groupby
from pandas.core.arrays import (
    DatetimeArray as DatetimeArray,
    ExtensionArray as ExtensionArray,
)
from pandas.core.construction import extract_array as extract_array
from pandas.core.dtypes.cast import find_common_type as find_common_type
from pandas.core.dtypes.common import (
    ensure_float64 as ensure_float64,
    ensure_int64 as ensure_int64,
    ensure_object as ensure_object,
    is_array_like as is_array_like,
    is_bool as is_bool,
    is_bool_dtype as is_bool_dtype,
    is_categorical_dtype as is_categorical_dtype,
    is_datetime64tz_dtype as is_datetime64tz_dtype,
    is_dtype_equal as is_dtype_equal,
    is_extension_array_dtype as is_extension_array_dtype,
    is_float_dtype as is_float_dtype,
    is_integer as is_integer,
    is_integer_dtype as is_integer_dtype,
    is_list_like as is_list_like,
    is_number as is_number,
    is_numeric_dtype as is_numeric_dtype,
    is_object_dtype as is_object_dtype,
    needs_i8_conversion as needs_i8_conversion,
)
from pandas.core.dtypes.generic import (
    ABCDataFrame as ABCDataFrame,
    ABCSeries as ABCSeries,
)
from pandas.core.dtypes.missing import (
    isna as isna,
    na_value_for_dtype as na_value_for_dtype,
)
from pandas.core.internals import concatenate_managers as concatenate_managers
from pandas.core.sorting import is_int64_overflow_possible as is_int64_overflow_possible
from pandas.errors import MergeError as MergeError
from pandas.util._decorators import Appender as Appender, Substitution as Substitution
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Union, Any, Hashable

def merge(
    left: Union[DataFrame, Series],
    right: Union[DataFrame, Series],
    how: str = ...,
    on: Union[IndexLabel, None] = ...,
    left_on: Union[IndexLabel, None] = ...,
    right_on: Union[IndexLabel, None] = ...,
    left_index: bool = ...,
    right_index: bool = ...,
    sort: bool = ...,
    suffixes: Suffixes = ...,
    copy: bool = ...,
    indicator: bool = ...,
    validate: Union[str, None] = ...,
) -> DataFrame: ...
def merge_ordered(
    left: DataFrame,
    right: DataFrame,
    on: Union[IndexLabel, None] = ...,
    left_on: Union[IndexLabel, None] = ...,
    right_on: Union[IndexLabel, None] = ...,
    left_by: Any | None = ...,
    right_by: Any | None = ...,
    fill_method: Union[str, None] = ...,
    suffixes: Suffixes = ...,
    how: str = ...,
) -> DataFrame: ...
def merge_asof(
    left: Union[DataFrame, Series],
    right: Union[DataFrame, Series],
    on: Union[IndexLabel, None] = ...,
    left_on: Union[IndexLabel, None] = ...,
    right_on: Union[IndexLabel, None] = ...,
    left_index: bool = ...,
    right_index: bool = ...,
    by: Any | None = ...,
    left_by: Any | None = ...,
    right_by: Any | None = ...,
    suffixes: Suffixes = ...,
    tolerance: Any | None = ...,
    allow_exact_matches: bool = ...,
    direction: str = ...,
) -> DataFrame: ...

class _MergeOperation:
    left: Any
    right: Any
    how: Any
    bm_axis: Any
    axis: Any
    on: Any
    left_on: Any
    right_on: Any
    copy: Any
    suffixes: Any
    sort: Any
    left_index: Any
    right_index: Any
    indicator: Any
    indicator_name: Any
    def __init__(
        self,
        left: Union[DataFrame, Series],
        right: Union[DataFrame, Series],
        how: str = ...,
        on: Union[IndexLabel, None] = ...,
        left_on: Union[IndexLabel, None] = ...,
        right_on: Union[IndexLabel, None] = ...,
        axis: int = ...,
        left_index: bool = ...,
        right_index: bool = ...,
        sort: bool = ...,
        suffixes: Suffixes = ...,
        copy: bool = ...,
        indicator: bool = ...,
        validate: Union[str, None] = ...,
    ) -> None: ...
    def get_result(self) -> DataFrame: ...

def get_join_indexers(
    left_keys, right_keys, sort: bool = ..., how: str = ..., **kwargs
) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]: ...
def restore_dropped_levels_multijoin(
    left: MultiIndex,
    right: MultiIndex,
    dropped_level_names,
    join_index: Index,
    lindexer: npt.NDArray[np.intp],
    rindexer: npt.NDArray[np.intp],
) -> tuple[list[Index], npt.NDArray[np.intp], list[Hashable]]: ...

class _OrderedMerge(_MergeOperation):
    fill_method: Any
    def __init__(
        self,
        left: Union[DataFrame, Series],
        right: Union[DataFrame, Series],
        on: Union[IndexLabel, None] = ...,
        left_on: Union[IndexLabel, None] = ...,
        right_on: Union[IndexLabel, None] = ...,
        left_index: bool = ...,
        right_index: bool = ...,
        axis: int = ...,
        suffixes: Suffixes = ...,
        copy: bool = ...,
        fill_method: Union[str, None] = ...,
        how: str = ...,
    ) -> None: ...
    def get_result(self) -> DataFrame: ...

class _AsOfMerge(_OrderedMerge):
    by: Any
    left_by: Any
    right_by: Any
    tolerance: Any
    allow_exact_matches: Any
    direction: Any
    def __init__(
        self,
        left: Union[DataFrame, Series],
        right: Union[DataFrame, Series],
        on: Union[IndexLabel, None] = ...,
        left_on: Union[IndexLabel, None] = ...,
        right_on: Union[IndexLabel, None] = ...,
        left_index: bool = ...,
        right_index: bool = ...,
        by: Any | None = ...,
        left_by: Any | None = ...,
        right_by: Any | None = ...,
        axis: int = ...,
        suffixes: Suffixes = ...,
        copy: bool = ...,
        fill_method: Union[str, None] = ...,
        how: str = ...,
        tolerance: Any | None = ...,
        allow_exact_matches: bool = ...,
        direction: str = ...,
    ) -> None: ...
