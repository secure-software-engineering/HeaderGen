import io
from pandas._typing import CompressionOptions as CompressionOptions, FilePath as FilePath, ReadBuffer as ReadBuffer, StorageOptions as StorageOptions, XMLParsers as XMLParsers
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.dtypes.common import is_list_like as is_list_like
from pandas.core.frame import DataFrame as DataFrame
from pandas.errors import AbstractMethodError as AbstractMethodError, ParserError as ParserError
from pandas.io.common import file_exists as file_exists, get_handle as get_handle, is_fsspec_url as is_fsspec_url, is_url as is_url, stringify_path as stringify_path
from pandas.io.parsers import TextParser as TextParser
from pandas.util._decorators import deprecate_nonkeyword_arguments as deprecate_nonkeyword_arguments, doc as doc
from typing import Union, Any, Sequence

class _XMLFrameParser:
    path_or_buffer: Any
    xpath: Any
    namespaces: Any
    elems_only: Any
    attrs_only: Any
    names: Any
    encoding: Any
    stylesheet: Any
    is_style: Any
    compression: Any
    storage_options: Any
    def __init__(self, path_or_buffer: Union[FilePath, ReadBuffer[bytes], ReadBuffer[str]], xpath: str, namespaces: Union[dict[str, str], None], elems_only: bool, attrs_only: bool, names: Union[Sequence[str], None], encoding: Union[str, None], stylesheet: Union[FilePath, ReadBuffer[bytes], ReadBuffer[str], None], compression: CompressionOptions, storage_options: StorageOptions) -> None: ...
    def parse_data(self) -> list[dict[str, Union[str, None]]]: ...

class _EtreeFrameParser(_XMLFrameParser):
    xml_doc: Any
    def parse_data(self) -> list[dict[str, Union[str, None]]]: ...

class _LxmlFrameParser(_XMLFrameParser):
    xml_doc: Any
    xsl_doc: Any
    def parse_data(self) -> list[dict[str, Union[str, None]]]: ...

def get_data_from_filepath(filepath_or_buffer: Union[FilePath, bytes, ReadBuffer[bytes], ReadBuffer[str]], encoding: Union[str, None], compression: CompressionOptions, storage_options: StorageOptions) -> Union[str, bytes, ReadBuffer[bytes], ReadBuffer[str]]: ...
def preprocess_data(data) -> Union[io.StringIO, io.BytesIO]: ...
def read_xml(path_or_buffer: Union[FilePath, ReadBuffer[bytes], ReadBuffer[str]], xpath: str = ..., namespaces: Union[dict[str, str], None] = ..., elems_only: bool = ..., attrs_only: bool = ..., names: Union[Sequence[str], None] = ..., encoding: Union[str, None] = ..., parser: XMLParsers = ..., stylesheet: Union[FilePath, ReadBuffer[bytes], ReadBuffer[str], None] = ..., compression: CompressionOptions = ..., storage_options: StorageOptions = ...) -> DataFrame: ...
