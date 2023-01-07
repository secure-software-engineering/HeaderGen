from .. import config_context as config_context
from typing import Any

class _VisualBlock:
    kind: Any
    estimators: Any
    dash_wrapped: Any
    names: Any
    name_details: Any
    def __init__(self, kind, estimators, *, names: Any | None = ..., name_details: Any | None = ..., dash_wrapped: bool = ...) -> None: ...

def estimator_html_repr(estimator): ...
