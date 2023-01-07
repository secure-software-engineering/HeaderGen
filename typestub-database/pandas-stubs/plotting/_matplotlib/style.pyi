from matplotlib.colors import Colormap as Colormap
from pandas.core.dtypes.common import is_list_like as is_list_like
from typing import Union, Collection, Sequence, Union

Color = Union[str, Sequence[float]]

def get_standard_colors(num_colors: int, colormap: Union[Colormap, None] = ..., color_type: str = ..., color: Union[dict[str, Color], Color, Collection[Color], None] = ...): ...
