from ._backend_tk import FigureCanvasTk as FigureCanvasTk, FigureManagerTk as FigureManagerTk, NavigationToolbar2Tk as NavigationToolbar2Tk, _BackendTk
from .backend_agg import FigureCanvasAgg as FigureCanvasAgg
from typing import Any

class FigureCanvasTkAgg(FigureCanvasAgg, FigureCanvasTk):
    def draw(self) -> None: ...
    def blit(self, bbox: Any | None = ...) -> None: ...

class _BackendTkAgg(_BackendTk):
    FigureCanvas: Any
