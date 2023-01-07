from pandas._libs.lib import is_list_like as is_list_like
from pandas.core.dtypes.generic import ABCIndex as ABCIndex, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import notna as notna
from typing import Union, Any

def to_time(arg, format: Any | None = ..., infer_time_format: bool = ..., errors: str = ...): ...
