from . import get_data_home as get_data_home
from ..utils import Bunch as Bunch, check_random_state as check_random_state
from ._base import RemoteFileMetadata as RemoteFileMetadata, load_descr as load_descr
from typing import Any

FACES: Any

def fetch_olivetti_faces(*, data_home: Any | None = ..., shuffle: bool = ..., random_state: int = ..., download_if_missing: bool = ..., return_X_y: bool = ...): ...
