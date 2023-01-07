from pandas import DataFrame as DataFrame
from pandas._typing import FilePath as FilePath, ReadBuffer as ReadBuffer
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.io.common import get_handle as get_handle

def read_orc(path: Union[FilePath, ReadBuffer[bytes]], columns: Union[list[str], None] = ..., **kwargs) -> DataFrame: ...
