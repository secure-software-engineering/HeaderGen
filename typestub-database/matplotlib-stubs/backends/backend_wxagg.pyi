from .backend_agg import FigureCanvasAgg as FigureCanvasAgg
from .backend_wx import FigureFrameWx as FigureFrameWx, _BackendWx, _FigureCanvasWxBase
from typing import Any

class FigureFrameWxAgg(FigureFrameWx):
    def get_canvas(self, fig): ...

class FigureCanvasWxAgg(FigureCanvasAgg, _FigureCanvasWxBase):
    bitmap: Any
    def draw(self, drawDC: Any | None = ...) -> None: ...
    def blit(self, bbox: Any | None = ...) -> None: ...

class _BackendWxAgg(_BackendWx):
    FigureCanvas: Any
