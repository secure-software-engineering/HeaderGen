from . import get_data_home as get_data_home
from ..utils import Bunch as Bunch
from ._base import RemoteFileMetadata as RemoteFileMetadata, load_descr as load_descr
from typing import Any

ARCHIVE: Any
logger: Any

def fetch_california_housing(*, data_home: Any | None = ..., download_if_missing: bool = ..., return_X_y: bool = ..., as_frame: bool = ...): ...
