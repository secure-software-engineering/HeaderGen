from tensorflow.python.debug.cli import debugger_cli_common as debugger_cli_common
from tensorflow.python.debug.lib import debug_data as debug_data
from typing import Any

BEGIN_INDICES_KEY: str
OMITTED_INDICES_KEY: str
DEFAULT_TENSOR_ELEMENT_HIGHLIGHT_FONT_ATTR: str

class HighlightOptions:
    criterion: Any
    description: Any
    font_attr: Any
    def __init__(self, criterion, description: Any | None = ..., font_attr=...) -> None: ...

def format_tensor(tensor, tensor_label, include_metadata: bool = ..., auxiliary_message: Any | None = ..., include_numeric_summary: bool = ..., np_printoptions: Any | None = ..., highlight_options: Any | None = ...): ...
def locate_tensor_element(formatted, indices): ...
def numeric_summary(tensor): ...
