from . import backend_cairo as backend_cairo, backend_gtk4 as backend_gtk4
from .backend_gtk4 import Gtk as Gtk, _BackendGTK4
from typing import Any

class RendererGTK4Cairo(backend_cairo.RendererCairo):
    def set_context(self, ctx) -> None: ...

class FigureCanvasGTK4Cairo(backend_gtk4.FigureCanvasGTK4, backend_cairo.FigureCanvasCairo):
    def __init__(self, figure) -> None: ...
    def on_draw_event(self, widget, ctx) -> None: ...

class _BackendGTK4Cairo(_BackendGTK4):
    FigureCanvas: Any
