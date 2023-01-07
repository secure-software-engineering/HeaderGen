from typing import Any

class __getattr__:
    STYLE_FILE_PATTERN: Any

def use(style) -> None: ...
def context(style, after_reset: bool = ...) -> None: ...

library: Any
available: Any

def reload_library() -> None: ...
