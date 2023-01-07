from . import backend_cairo as backend_cairo, backend_gtk3 as backend_gtk3
from .backend_gtk3 import Gtk as Gtk, _BackendGTK3
from typing import Any

class RendererGTK3Cairo(backend_cairo.RendererCairo):
    def set_context(self, ctx) -> None: ...

class FigureCanvasGTK3Cairo(backend_gtk3.FigureCanvasGTK3, backend_cairo.FigureCanvasCairo):
    def __init__(self, figure) -> None: ...
    def on_draw_event(self, widget, ctx) -> None: ...

class _BackendGTK3Cairo(_BackendGTK3):
    FigureCanvas: Any
