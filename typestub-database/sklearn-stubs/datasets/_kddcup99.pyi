from . import get_data_home as get_data_home
from ..utils import Bunch as Bunch, check_random_state as check_random_state
from ._base import RemoteFileMetadata as RemoteFileMetadata, load_descr as load_descr
from typing import Any

ARCHIVE: Any
ARCHIVE_10_PERCENT: Any
logger: Any

def fetch_kddcup99(*, subset: Any | None = ..., data_home: Any | None = ..., shuffle: bool = ..., random_state: Any | None = ..., percent10: bool = ..., download_if_missing: bool = ..., return_X_y: bool = ..., as_frame: bool = ...): ...
