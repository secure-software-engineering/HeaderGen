import enum
from matplotlib import cbook as cbook
from matplotlib._pylab_helpers import Gcf as Gcf
from typing import Any

class Cursors(enum.IntEnum):
    POINTER: Any
    HAND: Any
    SELECT_REGION: Any
    MOVE: Any
    WAIT: Any
    RESIZE_HORIZONTAL: Any
    RESIZE_VERTICAL: Any
cursors = Cursors

class ToolBase:
    default_keymap: Any
    description: Any
    image: Any
    def __init__(self, toolmanager, name) -> None: ...
    name: Any
    toolmanager: Any
    canvas: Any
    @property
    def figure(self): ...
    @figure.setter
    def figure(self, figure) -> None: ...
    set_figure: Any
    def trigger(self, sender, event, data: Any | None = ...) -> None: ...
    def destroy(self) -> None: ...

class ToolToggleBase(ToolBase):
    radio_group: Any
    cursor: Any
    default_toggled: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def trigger(self, sender, event, data: Any | None = ...) -> None: ...
    def enable(self, event: Any | None = ...) -> None: ...
    def disable(self, event: Any | None = ...) -> None: ...
    @property
    def toggled(self): ...
    def set_figure(self, figure) -> None: ...

class SetCursorBase(ToolBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def set_figure(self, figure) -> None: ...
    def set_cursor(self, cursor) -> None: ...
ToolSetCursor = SetCursorBase

class ToolCursorPosition(ToolBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def set_figure(self, figure) -> None: ...
    def send_message(self, event) -> None: ...

class RubberbandBase(ToolBase):
    def trigger(self, sender, event, data) -> None: ...
    def draw_rubberband(self, *data) -> None: ...
    def remove_rubberband(self) -> None: ...

class ToolQuit(ToolBase):
    description: str
    default_keymap: Any
    def trigger(self, sender, event, data: Any | None = ...) -> None: ...

class ToolQuitAll(ToolBase):
    description: str
    default_keymap: Any
    def trigger(self, sender, event, data: Any | None = ...) -> None: ...

class ToolGrid(ToolBase):
    description: str
    default_keymap: Any
    def trigger(self, sender, event, data: Any | None = ...) -> None: ...

class ToolMinorGrid(ToolBase):
    description: str
    default_keymap: Any
    def trigger(self, sender, event, data: Any | None = ...) -> None: ...

class ToolFullScreen(ToolToggleBase):
    description: str
    default_keymap: Any
    def enable(self, event) -> None: ...
    def disable(self, event) -> None: ...

class AxisScaleBase(ToolToggleBase):
    def trigger(self, sender, event, data: Any | None = ...) -> None: ...
    def enable(self, event) -> None: ...
    def disable(self, event) -> None: ...

class ToolYScale(AxisScaleBase):
    description: str
    default_keymap: Any
    def set_scale(self, ax, scale) -> None: ...

class ToolXScale(AxisScaleBase):
    description: str
    default_keymap: Any
    def set_scale(self, ax, scale) -> None: ...

class ToolViewsPositions(ToolBase):
    views: Any
    positions: Any
    home_views: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def add_figure(self, figure): ...
    def clear(self, figure) -> None: ...
    def update_view(self) -> None: ...
    def push_current(self, figure: Any | None = ...) -> None: ...
    def update_home_views(self, figure: Any | None = ...) -> None: ...
    def home(self) -> None: ...
    def back(self) -> None: ...
    def forward(self) -> None: ...

class ViewsPositionsBase(ToolBase):
    def trigger(self, sender, event, data: Any | None = ...) -> None: ...

class ToolHome(ViewsPositionsBase):
    description: str
    image: str
    default_keymap: Any

class ToolBack(ViewsPositionsBase):
    description: str
    image: str
    default_keymap: Any

class ToolForward(ViewsPositionsBase):
    description: str
    image: str
    default_keymap: Any

class ConfigureSubplotsBase(ToolBase):
    description: str
    image: str

class SaveFigureBase(ToolBase):
    description: str
    image: str
    default_keymap: Any

class ZoomPanBase(ToolToggleBase):
    base_scale: float
    scrollthresh: float
    lastscroll: Any
    def __init__(self, *args) -> None: ...
    def enable(self, event) -> None: ...
    def disable(self, event) -> None: ...
    def trigger(self, sender, event, data: Any | None = ...) -> None: ...
    def scroll_zoom(self, event) -> None: ...

class ToolZoom(ZoomPanBase):
    description: str
    image: str
    default_keymap: Any
    cursor: Any
    radio_group: str
    def __init__(self, *args) -> None: ...

class ToolPan(ZoomPanBase):
    default_keymap: Any
    description: str
    image: str
    cursor: Any
    radio_group: str
    def __init__(self, *args) -> None: ...

class ToolHelpBase(ToolBase):
    description: str
    default_keymap: Any
    image: str
    @staticmethod
    def format_shortcut(key_sequence): ...

class ToolCopyToClipboardBase(ToolBase):
    description: str
    default_keymap: Any
    def trigger(self, *args, **kwargs) -> None: ...

default_tools: Any
default_toolbar_tools: Any

def add_tools_to_manager(toolmanager, tools=...) -> None: ...
def add_tools_to_container(container, tools=...) -> None: ...
