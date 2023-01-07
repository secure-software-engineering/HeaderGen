from pandas._typing import StorageOptions as StorageOptions
from pandas.io.excel._base import ExcelWriter as ExcelWriter
from pandas.io.excel._util import combine_kwargs as combine_kwargs, validate_freeze_panes as validate_freeze_panes
from typing import Union, Any
from xlwt import XFStyle as XFStyle

class XlwtWriter(ExcelWriter):
    engine: str
    supported_extensions: Any
    book: Any
    fm_datetime: Any
    fm_date: Any
    def __init__(self, path, engine: Any | None = ..., date_format: Any | None = ..., datetime_format: Any | None = ..., encoding: Any | None = ..., mode: str = ..., storage_options: StorageOptions = ..., if_sheet_exists: Union[str, None] = ..., engine_kwargs: Union[dict[str, Any], None] = ..., **kwargs) -> None: ...
    def save(self) -> None: ...
    def write_cells(self, cells, sheet_name: Any | None = ..., startrow: int = ..., startcol: int = ..., freeze_panes: Any | None = ...) -> None: ...
