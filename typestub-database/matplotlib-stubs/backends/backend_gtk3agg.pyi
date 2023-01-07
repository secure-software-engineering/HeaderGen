from . import backend_agg as backend_agg, backend_cairo as backend_cairo, backend_gtk3 as backend_gtk3
from .. import cbook as cbook
from .backend_cairo import cairo as cairo
from .backend_gtk3 import Gtk as Gtk, _BackendGTK3
from matplotlib import transforms as transforms
from typing import Any

class FigureCanvasGTK3Agg(backend_gtk3.FigureCanvasGTK3, backend_agg.FigureCanvasAgg):
    def __init__(self, figure) -> None: ...
    def on_draw_event(self, widget, ctx): ...
    def blit(self, bbox: Any | None = ...) -> None: ...
    def draw(self) -> None: ...

class FigureManagerGTK3Agg(backend_gtk3.FigureManagerGTK3): ...

class _BackendGTK3Cairo(_BackendGTK3):
    FigureCanvas: Any
    FigureManager: Any
