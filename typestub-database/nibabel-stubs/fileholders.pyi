import io

from _typeshed import Incomplete

from .openers import ImageOpener as ImageOpener

class FileHolderError(Exception): ...

class FileHolder:
    filename: Incomplete
    fileobj: Incomplete
    pos: Incomplete
    def __init__(
        self,
        filename: str | None = None,
        fileobj: io.IOBase | None = None,
        pos: int = 0,
    ) -> None: ...
    def get_prepare_fileobj(self, *args, **kwargs) -> ImageOpener: ...
    def same_file_as(self, other: FileHolder) -> bool: ...
    @property
    def file_like(self) -> str | io.IOBase | None: ...

FileMap: Incomplete

def copy_file_map(file_map: FileMap) -> FileMap: ...
