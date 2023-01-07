from matplotlib import cbook as cbook
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase, FigureManagerBase as FigureManagerBase, NavigationToolbar2 as NavigationToolbar2, TimerBase as TimerBase, _Backend
from matplotlib.backends import _macosx
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvasAgg
from matplotlib.figure import Figure as Figure
from matplotlib.widgets import SubplotTool as SubplotTool
from typing import Any

class TimerMac(_macosx.Timer, TimerBase): ...

class FigureCanvasMac(_macosx.FigureCanvas, FigureCanvasAgg):
    required_interactive_framework: str
    def __init__(self, figure) -> None: ...
    def set_cursor(self, cursor) -> None: ...
    def draw(self) -> None: ...
    def blit(self, bbox: Any | None = ...) -> None: ...
    def resize(self, width, height) -> None: ...

class FigureManagerMac(_macosx.FigureManager, FigureManagerBase):
    toolbar: Any
    def __init__(self, canvas, num) -> None: ...
    def close(self) -> None: ...

class NavigationToolbar2Mac(_macosx.NavigationToolbar2, NavigationToolbar2):
    canvas: Any
    def __init__(self, canvas) -> None: ...
    def draw_rubberband(self, event, x0, y0, x1, y1) -> None: ...
    def remove_rubberband(self) -> None: ...
    def save_figure(self, *args) -> None: ...
    def prepare_configure_subplots(self): ...
    def set_message(self, message) -> None: ...

class _BackendMac(_Backend):
    FigureCanvas: Any
    FigureManager: Any
    @staticmethod
    def mainloop() -> None: ...
