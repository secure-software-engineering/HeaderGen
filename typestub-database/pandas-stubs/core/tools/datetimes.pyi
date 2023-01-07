import numpy as np
from datetime import datetime
from pandas import Series as Series
from pandas._libs import tslib as tslib
from pandas._libs.tslibs import OutOfBoundsDatetime as OutOfBoundsDatetime, Timedelta as Timedelta, Timestamp as Timestamp, conversion as conversion, iNaT as iNaT, nat_strings as nat_strings, parsing as parsing
from pandas._libs.tslibs.nattype import NaTType as NaTType
from pandas._libs.tslibs.parsing import DateParseError as DateParseError, format_is_iso as format_is_iso, guess_datetime_format as guess_datetime_format
from pandas._libs.tslibs.strptime import array_strptime as array_strptime
from pandas._typing import AnyArrayLike as AnyArrayLike, ArrayLike as ArrayLike, Timezone as Timezone
from pandas.arrays import DatetimeArray as DatetimeArray, IntegerArray as IntegerArray
from pandas.core import algorithms as algorithms
from pandas.core.algorithms import unique as unique
from pandas.core.arrays.datetimes import maybe_convert_dtype as maybe_convert_dtype, objects_to_datetime64ns as objects_to_datetime64ns, tz_to_dtype as tz_to_dtype
from pandas.core.construction import extract_array as extract_array
from pandas.core.dtypes.common import ensure_object as ensure_object, is_datetime64_dtype as is_datetime64_dtype, is_datetime64_ns_dtype as is_datetime64_ns_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_float as is_float, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_numeric_dtype as is_numeric_dtype, is_scalar as is_scalar
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import notna as notna
from pandas.core.indexes.base import Index as Index
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Union, Any, TypeVar, Union, overload

ArrayConvertible: Any
Scalar = Union[int, float, str]
DatetimeScalar = TypeVar('DatetimeScalar', Scalar, datetime)
DatetimeScalarOrArrayConvertible = Union[DatetimeScalar, ArrayConvertible]
start_caching_at: int

def should_cache(arg: ArrayConvertible, unique_share: float = ..., check_count: Union[int, None] = ...) -> bool: ...
@overload
def to_datetime(arg: DatetimeScalar, errors: str = ..., dayfirst: bool = ..., yearfirst: bool = ..., utc: Union[bool, None] = ..., format: Union[str, None] = ..., exact: bool = ..., unit: Union[str, None] = ..., infer_datetime_format: bool = ..., origin=..., cache: bool = ...) -> Union[DatetimeScalar, NaTType]: ...
@overload
def to_datetime(arg: Series, errors: str = ..., dayfirst: bool = ..., yearfirst: bool = ..., utc: Union[bool, None] = ..., format: Union[str, None] = ..., exact: bool = ..., unit: Union[str, None] = ..., infer_datetime_format: bool = ..., origin=..., cache: bool = ...) -> Series: ...
@overload
def to_datetime(arg: Union[list, tuple, np.ndarray], errors: str = ..., dayfirst: bool = ..., yearfirst: bool = ..., utc: Union[bool, None] = ..., format: Union[str, None] = ..., exact: bool = ..., unit: Union[str, None] = ..., infer_datetime_format: bool = ..., origin=..., cache: bool = ...) -> DatetimeIndex: ...
def to_time(arg, format: Any | None = ..., infer_time_format: bool = ..., errors: str = ...): ...
