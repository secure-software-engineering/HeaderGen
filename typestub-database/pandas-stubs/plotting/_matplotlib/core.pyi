import numpy as np
from matplotlib.artist import Artist as Artist
from matplotlib.axes import Axes as Axes
from matplotlib.axis import Axis as Axis
from pandas._typing import IndexLabel as IndexLabel
from pandas.core.dtypes.common import is_categorical_dtype as is_categorical_dtype, is_extension_array_dtype as is_extension_array_dtype, is_float as is_float, is_float_dtype as is_float_dtype, is_hashable as is_hashable, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_iterator as is_iterator, is_list_like as is_list_like, is_number as is_number, is_numeric_dtype as is_numeric_dtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCIndex as ABCIndex, ABCMultiIndex as ABCMultiIndex, ABCPeriodIndex as ABCPeriodIndex, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna, notna as notna
from pandas.core.frame import DataFrame as DataFrame
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.plotting._matplotlib.compat import mpl_ge_3_0_0 as mpl_ge_3_0_0
from pandas.plotting._matplotlib.converter import register_pandas_matplotlib_converters as register_pandas_matplotlib_converters
from pandas.plotting._matplotlib.groupby import reconstruct_data_with_by as reconstruct_data_with_by
from pandas.plotting._matplotlib.style import get_standard_colors as get_standard_colors
from pandas.plotting._matplotlib.timeseries import decorate_axes as decorate_axes, format_dateaxis as format_dateaxis, maybe_convert_index as maybe_convert_index, maybe_resample as maybe_resample, use_dynamic_x as use_dynamic_x
from pandas.plotting._matplotlib.tools import create_subplots as create_subplots, flatten_axes as flatten_axes, format_date_labels as format_date_labels, get_all_lines as get_all_lines, get_xlim as get_xlim, handle_shared_axes as handle_shared_axes, table as table
from pandas.util._decorators import cache_readonly as cache_readonly
from typing import Union, Any, Hashable

class MPLPlot:
    orientation: Union[str, None]
    axes: np.ndarray
    data: Any
    by: Any
    columns: Any
    kind: Any
    sort_columns: Any
    subplots: Any
    sharex: bool
    sharey: Any
    figsize: Any
    layout: Any
    xticks: Any
    yticks: Any
    xlim: Any
    ylim: Any
    title: Any
    use_index: Any
    xlabel: Any
    ylabel: Any
    fontsize: Any
    rot: Any
    grid: Any
    legend: Any
    legend_handles: Any
    legend_labels: Any
    logx: Any
    logy: Any
    loglog: Any
    label: Any
    style: Any
    mark_right: Any
    stacked: Any
    ax: Any
    fig: Any
    errors: Any
    secondary_y: Any
    colormap: Any
    table: Any
    include_bool: Any
    kwds: Any
    def __init__(self, data, kind: Any | None = ..., by: Union[IndexLabel, None] = ..., subplots: bool = ..., sharex: Any | None = ..., sharey: bool = ..., use_index: bool = ..., figsize: Any | None = ..., grid: Any | None = ..., legend: bool = ..., rot: Any | None = ..., ax: Any | None = ..., fig: Any | None = ..., title: Any | None = ..., xlim: Any | None = ..., ylim: Any | None = ..., xticks: Any | None = ..., yticks: Any | None = ..., xlabel: Union[Hashable, None] = ..., ylabel: Union[Hashable, None] = ..., sort_columns: bool = ..., fontsize: Any | None = ..., secondary_y: bool = ..., colormap: Any | None = ..., table: bool = ..., layout: Any | None = ..., include_bool: bool = ..., column: Union[IndexLabel, None] = ..., **kwds) -> None: ...
    @property
    def nseries(self) -> int: ...
    def draw(self) -> None: ...
    def generate(self) -> None: ...
    @property
    def result(self): ...
    @property
    def legend_title(self) -> Union[str, None]: ...
    def plt(self): ...
    @classmethod
    def get_default_ax(cls, ax) -> None: ...
    def on_right(self, i): ...

class PlanePlot(MPLPlot):
    x: Any
    y: Any
    def __init__(self, data, x, y, **kwargs) -> None: ...
    @property
    def nseries(self) -> int: ...

class ScatterPlot(PlanePlot):
    c: Any
    def __init__(self, data, x, y, s: Any | None = ..., c: Any | None = ..., **kwargs) -> None: ...

class HexBinPlot(PlanePlot):
    C: Any
    def __init__(self, data, x, y, C: Any | None = ..., **kwargs) -> None: ...

class LinePlot(MPLPlot):
    orientation: str
    data: Any
    x_compat: Any
    def __init__(self, data, **kwargs) -> None: ...

class AreaPlot(LinePlot):
    def __init__(self, data, **kwargs) -> None: ...

class BarPlot(MPLPlot):
    orientation: str
    bar_width: Any
    tick_pos: Any
    bottom: Any
    left: Any
    log: Any
    tickoffset: Any
    lim_offset: Any
    ax_pos: Any
    def __init__(self, data, **kwargs) -> None: ...

class BarhPlot(BarPlot):
    orientation: str

class PiePlot(MPLPlot):
    def __init__(self, data, kind: Any | None = ..., **kwargs) -> None: ...
