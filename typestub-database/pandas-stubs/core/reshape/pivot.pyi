from pandas import DataFrame as DataFrame
from pandas._typing import AggFuncType as AggFuncType, AggFuncTypeBase as AggFuncTypeBase, AggFuncTypeDict as AggFuncTypeDict, IndexLabel as IndexLabel
from pandas.core.dtypes.cast import maybe_downcast_to_dtype as maybe_downcast_to_dtype
from pandas.core.dtypes.common import is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_nested_list_like as is_nested_list_like, is_scalar as is_scalar
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.groupby import Grouper as Grouper
from pandas.core.indexes.api import Index as Index, MultiIndex as MultiIndex, get_objs_combined_axis as get_objs_combined_axis
from pandas.core.reshape.concat import concat as concat
from pandas.core.reshape.util import cartesian_product as cartesian_product
from pandas.core.series import Series as Series
from pandas.util._decorators import Appender as Appender, Substitution as Substitution
from typing import Union, Any

def pivot_table(data: DataFrame, values: Any | None = ..., index: Any | None = ..., columns: Any | None = ..., aggfunc: AggFuncType = ..., fill_value: Any | None = ..., margins: bool = ..., dropna: bool = ..., margins_name: str = ..., observed: bool = ..., sort: bool = ...) -> DataFrame: ...
def pivot(data: DataFrame, index: Union[IndexLabel, None] = ..., columns: Union[IndexLabel, None] = ..., values: Union[IndexLabel, None] = ...) -> DataFrame: ...
def crosstab(index, columns, values: Any | None = ..., rownames: Any | None = ..., colnames: Any | None = ..., aggfunc: Any | None = ..., margins: bool = ..., margins_name: str = ..., dropna: bool = ..., normalize: bool = ...) -> DataFrame: ...
