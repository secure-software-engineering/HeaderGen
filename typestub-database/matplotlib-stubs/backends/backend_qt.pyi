from . import qt_compat as qt_compat
from .qt_compat import QT_API as QT_API, QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from matplotlib import backend_tools as backend_tools, cbook as cbook
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase, FigureManagerBase as FigureManagerBase, MouseButton as MouseButton, NavigationToolbar2 as NavigationToolbar2, TimerBase as TimerBase, ToolContainerBase as ToolContainerBase, _Backend, cursors as cursors
from typing import Any

backend_version: Any
SPECIAL_KEYS: Any
cursord: Any
qApp: Any

class TimerQT(TimerBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __del__(self) -> None: ...

class FigureCanvasQT(QtWidgets.QWidget, FigureCanvasBase):
    required_interactive_framework: str
    buttond: Any
    def __init__(self, figure: Any | None = ...) -> None: ...
    def showEvent(self, event) -> None: ...
    def set_cursor(self, cursor) -> None: ...
    def enterEvent(self, event) -> None: ...
    def leaveEvent(self, event) -> None: ...
    def mouseEventCoords(self, pos): ...
    def mousePressEvent(self, event) -> None: ...
    def mouseDoubleClickEvent(self, event) -> None: ...
    def mouseMoveEvent(self, event) -> None: ...
    def mouseReleaseEvent(self, event) -> None: ...
    def wheelEvent(self, event) -> None: ...
    def keyPressEvent(self, event) -> None: ...
    def keyReleaseEvent(self, event) -> None: ...
    def resizeEvent(self, event) -> None: ...
    def sizeHint(self): ...
    def minumumSizeHint(self): ...
    def flush_events(self) -> None: ...
    def start_event_loop(self, timeout: int = ...) -> None: ...
    def stop_event_loop(self, event: Any | None = ...) -> None: ...
    def draw(self) -> None: ...
    def draw_idle(self) -> None: ...
    def blit(self, bbox: Any | None = ...) -> None: ...
    def drawRectangle(self, rect) -> None: ...

class MainWindow(QtWidgets.QMainWindow):
    closing: Any
    def closeEvent(self, event) -> None: ...

class FigureManagerQT(FigureManagerBase):
    window: Any
    toolbar: Any
    def __init__(self, canvas, num) -> None: ...
    def full_screen_toggle(self) -> None: ...
    def resize(self, width, height) -> None: ...
    def show(self) -> None: ...
    def destroy(self, *args) -> None: ...
    def get_window_title(self): ...
    def set_window_title(self, title) -> None: ...

class NavigationToolbar2QT(NavigationToolbar2, QtWidgets.QToolBar):
    message: Any
    toolitems: Any
    coordinates: Any
    locLabel: Any
    def __init__(self, canvas, parent, coordinates: bool = ...) -> None: ...
    def edit_parameters(self) -> None: ...
    def pan(self, *args) -> None: ...
    def zoom(self, *args) -> None: ...
    def set_message(self, s) -> None: ...
    def draw_rubberband(self, event, x0, y0, x1, y1) -> None: ...
    def remove_rubberband(self) -> None: ...
    def configure_subplots(self): ...
    def save_figure(self, *args) -> None: ...
    def set_history_buttons(self) -> None: ...

class SubplotToolQt(QtWidgets.QDialog):
    def __init__(self, targetfig, parent) -> None: ...
    def update_from_current_subplotpars(self) -> None: ...

class ToolbarQt(ToolContainerBase, QtWidgets.QToolBar):
    def __init__(self, toolmanager, parent) -> None: ...
    def add_toolitem(self, name, group, position, image_file, description, toggle) -> None: ...
    def toggle_toolitem(self, name, toggled) -> None: ...
    def remove_toolitem(self, name) -> None: ...
    def set_message(self, s) -> None: ...

class ConfigureSubplotsQt(backend_tools.ConfigureSubplotsBase):
    def trigger(self, *args) -> None: ...

class SaveFigureQt(backend_tools.SaveFigureBase):
    def trigger(self, *args) -> None: ...

class SetCursorQt(backend_tools.SetCursorBase):
    def set_cursor(self, cursor) -> None: ...

class RubberbandQt(backend_tools.RubberbandBase):
    def draw_rubberband(self, x0, y0, x1, y1) -> None: ...
    def remove_rubberband(self) -> None: ...

class HelpQt(backend_tools.ToolHelpBase):
    def trigger(self, *args) -> None: ...

class ToolCopyToClipboardQT(backend_tools.ToolCopyToClipboardBase):
    def trigger(self, *args, **kwargs) -> None: ...

class _BackendQT(_Backend):
    FigureCanvas: Any
    FigureManager: Any
    @staticmethod
    def mainloop() -> None: ...
