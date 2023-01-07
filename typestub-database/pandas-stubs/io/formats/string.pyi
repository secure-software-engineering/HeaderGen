from pandas.io.formats.format import DataFrameFormatter as DataFrameFormatter
from pandas.io.formats.printing import pprint_thing as pprint_thing
from typing import Union, Any

class StringFormatter:
    fmt: Any
    adj: Any
    frame: Any
    line_width: Any
    def __init__(self, fmt: DataFrameFormatter, line_width: Union[int, None] = ...) -> None: ...
    def to_string(self) -> str: ...
