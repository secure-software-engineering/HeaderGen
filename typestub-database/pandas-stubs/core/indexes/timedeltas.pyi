from pandas._libs import lib as lib
from pandas._libs.tslibs import Timedelta as Timedelta, to_offset as to_offset
from pandas._typing import DtypeObj as DtypeObj
from pandas.core.arrays.timedeltas import TimedeltaArray as TimedeltaArray
from pandas.core.dtypes.common import TD64NS_DTYPE as TD64NS_DTYPE, is_scalar as is_scalar, is_timedelta64_dtype as is_timedelta64_dtype
from pandas.core.indexes.base import Index as Index, maybe_extract_name as maybe_extract_name
from pandas.core.indexes.datetimelike import DatetimeTimedeltaMixin as DatetimeTimedeltaMixin
from pandas.core.indexes.extension import inherit_names as inherit_names
from typing import Union, Any

class TimedeltaIndex(DatetimeTimedeltaMixin):
    def __new__(cls, data: Any | None = ..., unit: Any | None = ..., freq=..., closed: Any | None = ..., dtype=..., copy: bool = ..., name: Any | None = ...): ...
    def get_loc(self, key, method: Any | None = ..., tolerance: Any | None = ...): ...
    @property
    def inferred_type(self) -> str: ...

def timedelta_range(start: Any | None = ..., end: Any | None = ..., periods: Union[int, None] = ..., freq: Any | None = ..., name: Any | None = ..., closed: Any | None = ...) -> TimedeltaIndex: ...
