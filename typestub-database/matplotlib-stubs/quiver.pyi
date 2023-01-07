import matplotlib.artist as martist
import matplotlib.collections as mcollections
from matplotlib import cbook as cbook, docstring as docstring, font_manager as font_manager
from matplotlib.patches import CirclePolygon as CirclePolygon
from typing import Any

class QuiverKey(martist.Artist):
    halign: Any
    valign: Any
    pivot: Any
    Q: Any
    X: Any
    Y: Any
    U: Any
    angle: Any
    coord: Any
    color: Any
    label: Any
    labelsep: Any
    labelpos: Any
    labelcolor: Any
    fontproperties: Any
    kw: Any
    text: Any
    zorder: Any
    def __init__(self, Q, X, Y, U, label, *, angle: int = ..., coordinates: str = ..., color: Any | None = ..., labelsep: float = ..., labelpos: str = ..., labelcolor: Any | None = ..., fontproperties: Any | None = ..., **kw) -> None: ...
    def remove(self) -> None: ...
    stale: bool
    def draw(self, renderer) -> None: ...
    def set_figure(self, fig) -> None: ...
    def contains(self, mouseevent): ...

class Quiver(mcollections.PolyCollection):
    X: Any
    Y: Any
    XY: Any
    N: Any
    scale: Any
    headwidth: Any
    headlength: Any
    headaxislength: Any
    minshaft: Any
    minlength: Any
    units: Any
    scale_units: Any
    angles: Any
    width: Any
    pivot: Any
    transform: Any
    polykw: Any
    def __init__(self, ax, *args, scale: Any | None = ..., headwidth: int = ..., headlength: int = ..., headaxislength: float = ..., minshaft: int = ..., minlength: int = ..., units: str = ..., scale_units: Any | None = ..., angles: str = ..., width: Any | None = ..., color: str = ..., pivot: str = ..., **kw) -> None: ...
    def remove(self) -> None: ...
    def get_datalim(self, transData): ...
    stale: bool
    def draw(self, renderer) -> None: ...
    U: Any
    V: Any
    Umask: Any
    def set_UVC(self, U, V, C: Any | None = ...) -> None: ...
    quiver_doc: Any

class Barbs(mcollections.PolyCollection):
    sizes: Any
    fill_empty: Any
    barb_increments: Any
    rounding: Any
    flip: Any
    x: Any
    y: Any
    def __init__(self, ax, *args, pivot: str = ..., length: int = ..., barbcolor: Any | None = ..., flagcolor: Any | None = ..., sizes: Any | None = ..., fill_empty: bool = ..., barb_increments: Any | None = ..., rounding: bool = ..., flip_barb: bool = ..., **kw) -> None: ...
    u: Any
    v: Any
    stale: bool
    def set_UVC(self, U, V, C: Any | None = ...) -> None: ...
    def set_offsets(self, xy) -> None: ...
    barbs_doc: Any
