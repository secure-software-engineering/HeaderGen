from ._backend_tk import FigureCanvasTk as FigureCanvasTk, _BackendTk
from .backend_cairo import FigureCanvasCairo as FigureCanvasCairo, RendererCairo as RendererCairo, cairo as cairo
from typing import Any

class FigureCanvasTkCairo(FigureCanvasCairo, FigureCanvasTk):
    def __init__(self, *args, **kwargs) -> None: ...
    def draw(self) -> None: ...

class _BackendTkCairo(_BackendTk):
    FigureCanvas: Any
