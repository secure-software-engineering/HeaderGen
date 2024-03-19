import tempfile
from collections.abc import Generator

from _typeshed import Incomplete

from .deprecated import deprecate_with_version as deprecate_with_version

class TemporaryDirectory(tempfile.TemporaryDirectory):
    def __init__(
        self, suffix: str = "", prefix=..., dir: Incomplete | None = None
    ) -> None: ...

def InTemporaryDirectory() -> Generator[Incomplete, None, None]: ...
def InGivenDirectory(
    path: Incomplete | None = None,
) -> Generator[Incomplete, None, None]: ...
