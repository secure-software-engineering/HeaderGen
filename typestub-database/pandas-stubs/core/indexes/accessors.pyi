import numpy as np
from pandas import Series as Series
from pandas.core.accessor import PandasDelegate as PandasDelegate, delegate_names as delegate_names
from pandas.core.arrays import DatetimeArray as DatetimeArray, PeriodArray as PeriodArray, TimedeltaArray as TimedeltaArray
from pandas.core.base import NoNewAttributesMixin as NoNewAttributesMixin, PandasObject as PandasObject
from pandas.core.dtypes.common import is_categorical_dtype as is_categorical_dtype, is_datetime64_dtype as is_datetime64_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_period_dtype as is_period_dtype, is_timedelta64_dtype as is_timedelta64_dtype
from pandas.core.dtypes.generic import ABCSeries as ABCSeries
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex as TimedeltaIndex
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Union, Any

class Properties(PandasDelegate, PandasObject, NoNewAttributesMixin):
    orig: Any
    name: Any
    def __init__(self, data: Series, orig) -> None: ...

class DatetimeProperties(Properties):
    def to_pydatetime(self) -> np.ndarray: ...
    @property
    def freq(self): ...
    def isocalendar(self): ...
    @property
    def weekofyear(self): ...
    week: Any

class TimedeltaProperties(Properties):
    def to_pytimedelta(self) -> np.ndarray: ...
    @property
    def components(self): ...
    @property
    def freq(self): ...

class PeriodProperties(Properties): ...

class CombinedDatetimelikeProperties(DatetimeProperties, TimedeltaProperties, PeriodProperties):
    def __new__(cls, data: Series): ...
