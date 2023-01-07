from .backend_cairo import FigureCanvasCairo as FigureCanvasCairo, RendererCairo as RendererCairo, cairo as cairo
from .backend_wx import FigureFrameWx as FigureFrameWx, _BackendWx, _FigureCanvasWxBase
from typing import Any

class FigureFrameWxCairo(FigureFrameWx):
    def get_canvas(self, fig): ...

class FigureCanvasWxCairo(_FigureCanvasWxBase, FigureCanvasCairo):
    def __init__(self, parent, id, figure) -> None: ...
    bitmap: Any
    def draw(self, drawDC: Any | None = ...) -> None: ...

class _BackendWxCairo(_BackendWx):
    FigureCanvas: Any
