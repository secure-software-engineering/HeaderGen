from ._backend_gtk import _BackendGTK, _NavigationToolbar2GTK, backend_version as backend_version
from gi.repository import Gtk
from matplotlib import backend_tools as backend_tools, cbook as cbook
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase, FigureManagerBase as FigureManagerBase, NavigationToolbar2 as NavigationToolbar2, TimerBase as TimerBase, ToolContainerBase as ToolContainerBase
from matplotlib.backend_tools import Cursors as Cursors
from matplotlib.figure import Figure as Figure
from matplotlib.widgets import SubplotTool as SubplotTool
from typing import Any

class __getattr__:
    @property
    def cursord(self): ...

class FigureCanvasGTK3(Gtk.DrawingArea, FigureCanvasBase):
    required_interactive_framework: str
    event_mask: Any
    def __init__(self, figure: Any | None = ...) -> None: ...
    def destroy(self) -> None: ...
    def set_cursor(self, cursor) -> None: ...
    def scroll_event(self, widget, event): ...
    def button_press_event(self, widget, event): ...
    def button_release_event(self, widget, event): ...
    def key_press_event(self, widget, event): ...
    def key_release_event(self, widget, event): ...
    def motion_notify_event(self, widget, event): ...
    def leave_notify_event(self, widget, event) -> None: ...
    def enter_notify_event(self, widget, event) -> None: ...
    def size_allocate(self, widget, allocation) -> None: ...
    def configure_event(self, widget, event): ...
    def on_draw_event(self, widget, ctx) -> None: ...
    def draw(self) -> None: ...
    def draw_idle(self): ...
    def flush_events(self) -> None: ...

class FigureManagerGTK3(FigureManagerBase):
    window: Any
    vbox: Any
    toolbar: Any
    def __init__(self, canvas, num): ...
    def destroy(self, *args) -> None: ...
    def show(self) -> None: ...
    def full_screen_toggle(self) -> None: ...
    def get_window_title(self): ...
    def set_window_title(self, title) -> None: ...
    def resize(self, width, height) -> None: ...

class NavigationToolbar2GTK3(_NavigationToolbar2GTK, Gtk.Toolbar):
    win: Any
    message: Any
    def __init__(self, canvas, window) -> None: ...
    def save_figure(self, *args) -> None: ...

class ToolbarGTK3(ToolContainerBase, Gtk.Box):
    def __init__(self, toolmanager) -> None: ...
    def add_toolitem(self, name, group, position, image_file, description, toggle) -> None: ...
    def toggle_toolitem(self, name, toggled) -> None: ...
    def remove_toolitem(self, name) -> None: ...
    def set_message(self, s) -> None: ...

class SaveFigureGTK3(backend_tools.SaveFigureBase):
    def trigger(self, *args, **kwargs): ...

class SetCursorGTK3(backend_tools.SetCursorBase):
    def set_cursor(self, cursor) -> None: ...

class HelpGTK3(backend_tools.ToolHelpBase):
    def trigger(self, *args) -> None: ...

class ToolCopyToClipboardGTK3(backend_tools.ToolCopyToClipboardBase):
    def trigger(self, *args, **kwargs) -> None: ...

icon_filename: str
window_icon: Any

def error_msg_gtk(msg, parent: Any | None = ...) -> None: ...
Toolbar = ToolbarGTK3

class _BackendGTK3(_BackendGTK):
    FigureCanvas: Any
    FigureManager: Any
