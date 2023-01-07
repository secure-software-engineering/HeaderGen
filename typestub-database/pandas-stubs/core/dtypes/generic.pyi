from pandas import Categorical as Categorical, CategoricalIndex as CategoricalIndex, DataFrame as DataFrame, DatetimeIndex as DatetimeIndex, Float64Index as Float64Index, Index as Index, Int64Index as Int64Index, IntervalIndex as IntervalIndex, MultiIndex as MultiIndex, PeriodIndex as PeriodIndex, RangeIndex as RangeIndex, Series as Series, TimedeltaIndex as TimedeltaIndex, UInt64Index as UInt64Index
from pandas.core.arrays import DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray, PandasArray as PandasArray, PeriodArray as PeriodArray, TimedeltaArray as TimedeltaArray
from pandas.core.generic import NDFrame as NDFrame
from typing import Union, Any

def create_pandas_abc_type(name, attr, comp): ...

ABCInt64Index: Any
ABCUInt64Index: Any
ABCRangeIndex: Any
ABCFloat64Index: Any
ABCMultiIndex: Any
ABCDatetimeIndex: Any
ABCTimedeltaIndex: Any
ABCPeriodIndex: Any
ABCCategoricalIndex: Any
ABCIntervalIndex: Any
ABCIndex: Any
ABCNDFrame: Any
ABCSeries: Any
ABCDataFrame: Any
ABCCategorical: Any
ABCDatetimeArray: Any
ABCTimedeltaArray: Any
ABCPeriodArray: Any
ABCExtensionArray: Any
ABCPandasArray: Any
