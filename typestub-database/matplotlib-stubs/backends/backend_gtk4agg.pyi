from . import backend_agg as backend_agg, backend_cairo as backend_cairo, backend_gtk4 as backend_gtk4
from .. import cbook as cbook
from .backend_cairo import cairo as cairo
from .backend_gtk4 import Gtk as Gtk, _BackendGTK4
from typing import Any

class FigureCanvasGTK4Agg(backend_gtk4.FigureCanvasGTK4, backend_agg.FigureCanvasAgg):
    def __init__(self, figure) -> None: ...
    def on_draw_event(self, widget, ctx): ...
    def draw(self) -> None: ...

class FigureManagerGTK4Agg(backend_gtk4.FigureManagerGTK4): ...

class _BackendGTK4Agg(_BackendGTK4):
    FigureCanvas: Any
    FigureManager: Any
