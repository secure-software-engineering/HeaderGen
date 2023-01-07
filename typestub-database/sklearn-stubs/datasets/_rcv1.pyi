from . import get_data_home as get_data_home
from ..utils import Bunch as Bunch
from ._base import RemoteFileMetadata as RemoteFileMetadata, load_descr as load_descr
from ._svmlight_format_io import load_svmlight_files as load_svmlight_files
from typing import Any

XY_METADATA: Any
TOPICS_METADATA: Any
logger: Any

def fetch_rcv1(*, data_home: Any | None = ..., subset: str = ..., download_if_missing: bool = ..., random_state: Any | None = ..., shuffle: bool = ..., return_X_y: bool = ...): ...
