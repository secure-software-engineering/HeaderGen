from pandas._libs import lib as lib
from pandas._libs.tslibs import NaT as NaT, NaTType as NaTType
from pandas._libs.tslibs.timedeltas import Timedelta as Timedelta, parse_timedelta_unit as parse_timedelta_unit
from pandas.core.arrays.timedeltas import sequence_to_td64ns as sequence_to_td64ns
from pandas.core.dtypes.common import is_list_like as is_list_like
from pandas.core.dtypes.generic import ABCIndex as ABCIndex, ABCSeries as ABCSeries
from typing import Union, Any

def to_timedelta(arg, unit: Any | None = ..., errors: str = ...): ...
