from tensorflow.python.debug.cli import debugger_cli_common as debugger_cli_common
from typing import Any

RL: Any

class NavigationHistoryItem:
    command: Any
    screen_output: Any
    scroll_position: Any
    def __init__(self, command, screen_output, scroll_position) -> None: ...

class CursesNavigationHistory:
    BACK_ARROW_TEXT: str
    FORWARD_ARROW_TEXT: str
    def __init__(self, capacity) -> None: ...
    def add_item(self, command, screen_output, scroll_position) -> None: ...
    def update_scroll_position(self, new_scroll_position) -> None: ...
    def size(self): ...
    def pointer(self): ...
    def go_back(self): ...
    def go_forward(self): ...
    def can_go_back(self): ...
    def can_go_forward(self): ...
    def render(self, max_length, backward_command, forward_command, latest_command_attribute: str = ..., old_command_attribute: str = ...): ...
