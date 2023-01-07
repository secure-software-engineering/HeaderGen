import numpy as np
from pandas._libs.arrays import NDArrayBacked as NDArrayBacked
from pandas._libs.tslibs import BaseOffset as BaseOffset, NaT as NaT, NaTType as NaTType, Timedelta as Timedelta, delta_to_nanoseconds as delta_to_nanoseconds, iNaT as iNaT, parsing as parsing, to_offset as to_offset
from pandas._libs.tslibs.dtypes import FreqGroup as FreqGroup
from pandas._libs.tslibs.fields import isleapyear_arr as isleapyear_arr
from pandas._libs.tslibs.offsets import Tick as Tick, delta_to_tick as delta_to_tick
from pandas._libs.tslibs.period import DIFFERENT_FREQ as DIFFERENT_FREQ, IncompatibleFrequency as IncompatibleFrequency, Period as Period, get_period_field_arr as get_period_field_arr, period_asfreq_arr as period_asfreq_arr
from pandas._typing import AnyArrayLike as AnyArrayLike, Dtype as Dtype, NpDtype as NpDtype, NumpySorter as NumpySorter, NumpyValueArrayLike as NumpyValueArrayLike, npt as npt
from pandas.core.arrays import DatetimeArray as DatetimeArray, datetimelike as dtl
from pandas.core.arrays.base import ExtensionArray as ExtensionArray
from pandas.core.dtypes.common import TD64NS_DTYPE as TD64NS_DTYPE, ensure_object as ensure_object, is_datetime64_any_dtype as is_datetime64_any_dtype, is_datetime64_dtype as is_datetime64_dtype, is_dtype_equal as is_dtype_equal, is_float_dtype as is_float_dtype, is_integer_dtype as is_integer_dtype, is_period_dtype as is_period_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import PeriodDtype as PeriodDtype
from pandas.core.dtypes.generic import ABCIndex as ABCIndex, ABCPeriodIndex as ABCPeriodIndex, ABCSeries as ABCSeries, ABCTimedeltaArray as ABCTimedeltaArray
from pandas.core.dtypes.missing import isna as isna, notna as notna
from pandas.util._decorators import cache_readonly as cache_readonly, doc as doc
from typing import Union, Any, Literal, Sequence

class PeriodArray(dtl.DatelikeOps):
    __array_priority__: int
    def __init__(self, values, dtype: Union[Dtype, None] = ..., freq: Any | None = ..., copy: bool = ...) -> None: ...
    def dtype(self) -> PeriodDtype: ...
    @property
    def freq(self) -> BaseOffset: ...
    def __array__(self, dtype: Union[NpDtype, None] = ...) -> np.ndarray: ...
    def __arrow_array__(self, type: Any | None = ...): ...
    year: Any
    month: Any
    day: Any
    hour: Any
    minute: Any
    second: Any
    weekofyear: Any
    week: Any
    day_of_week: Any
    dayofweek: Any
    weekday: Any
    dayofyear: Any
    day_of_year: Any
    quarter: Any
    qyear: Any
    days_in_month: Any
    daysinmonth: Any
    @property
    def is_leap_year(self) -> np.ndarray: ...
    def to_timestamp(self, freq: Any | None = ..., how: str = ...) -> DatetimeArray: ...
    def asfreq(self, freq: Any | None = ..., how: str = ...) -> PeriodArray: ...
    def astype(self, dtype, copy: bool = ...): ...
    def searchsorted(self, value: Union[NumpyValueArrayLike, ExtensionArray], side: Literal[left, right] = ..., sorter: NumpySorter = ...) -> Union[npt.NDArray[np.intp], np.intp]: ...
    def fillna(self, value: Any | None = ..., method: Any | None = ..., limit: Any | None = ...) -> PeriodArray: ...
    @property
    def start_time(self) -> DatetimeArray: ...
    @property
    def end_time(self) -> DatetimeArray: ...

def raise_on_incompatible(left, right): ...
def period_array(data: Union[Sequence[Union[Period, str, None]], AnyArrayLike], freq: Union[str, Tick, None] = ..., copy: bool = ...) -> PeriodArray: ...
def validate_dtype_freq(dtype, freq): ...
def dt64arr_to_periodarr(data, freq, tz: Any | None = ...): ...
