from matplotlib.axes import Axes as Axes
from pandas.core.dtypes.common import is_integer as is_integer, is_list_like as is_list_like
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCIndex as ABCIndex
from pandas.core.dtypes.missing import isna as isna, remove_na_arraylike as remove_na_arraylike
from pandas.core.frame import DataFrame as DataFrame
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.plotting._matplotlib.core import LinePlot as LinePlot, MPLPlot as MPLPlot
from pandas.plotting._matplotlib.groupby import create_iter_data_given_by as create_iter_data_given_by, reformat_hist_y_given_by as reformat_hist_y_given_by
from pandas.plotting._matplotlib.tools import create_subplots as create_subplots, flatten_axes as flatten_axes, maybe_adjust_figure as maybe_adjust_figure, set_ticks_props as set_ticks_props
from typing import Union, Any

class HistPlot(LinePlot):
    bins: Any
    bottom: Any
    def __init__(self, data, bins: int = ..., bottom: int = ..., **kwargs) -> None: ...
    @property
    def orientation(self): ...

class KdePlot(HistPlot):
    orientation: str
    bw_method: Any
    ind: Any
    def __init__(self, data, bw_method: Any | None = ..., ind: Any | None = ..., **kwargs) -> None: ...

def hist_series(self, by: Any | None = ..., ax: Any | None = ..., grid: bool = ..., xlabelsize: Any | None = ..., xrot: Any | None = ..., ylabelsize: Any | None = ..., yrot: Any | None = ..., figsize: Any | None = ..., bins: int = ..., legend: bool = ..., **kwds): ...
def hist_frame(data, column: Any | None = ..., by: Any | None = ..., grid: bool = ..., xlabelsize: Any | None = ..., xrot: Any | None = ..., ylabelsize: Any | None = ..., yrot: Any | None = ..., ax: Any | None = ..., sharex: bool = ..., sharey: bool = ..., figsize: Any | None = ..., layout: Any | None = ..., bins: int = ..., legend: bool = ..., **kwds): ...
