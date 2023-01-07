from pandas._typing import StorageOptions as StorageOptions
from pandas.io.excel._base import ExcelWriter as ExcelWriter
from pandas.io.excel._util import combine_kwargs as combine_kwargs, validate_freeze_panes as validate_freeze_panes
from pandas.io.formats.excel import ExcelCell as ExcelCell
from typing import Union, Any

class ODSWriter(ExcelWriter):
    engine: str
    supported_extensions: Any
    book: Any
    def __init__(self, path: str, engine: Union[str, None] = ..., date_format: Any | None = ..., datetime_format: Any | None = ..., mode: str = ..., storage_options: StorageOptions = ..., if_sheet_exists: Union[str, None] = ..., engine_kwargs: Union[dict[str, Any], None] = ..., **kwargs) -> None: ...
    def save(self) -> None: ...
    def write_cells(self, cells: list[ExcelCell], sheet_name: Union[str, None] = ..., startrow: int = ..., startcol: int = ..., freeze_panes: Union[tuple[int, int], None] = ...) -> None: ...
