from . import get_data_home as get_data_home, load_files as load_files
from .. import preprocessing as preprocessing
from ..feature_extraction.text import CountVectorizer as CountVectorizer
from ..utils import Bunch as Bunch, check_random_state as check_random_state
from ._base import RemoteFileMetadata as RemoteFileMetadata, load_descr as load_descr
from typing import Any

logger: Any
ARCHIVE: Any
CACHE_NAME: str
TRAIN_FOLDER: str
TEST_FOLDER: str

def strip_newsgroup_header(text): ...
def strip_newsgroup_quoting(text): ...
def strip_newsgroup_footer(text): ...
def fetch_20newsgroups(*, data_home: Any | None = ..., subset: str = ..., categories: Any | None = ..., shuffle: bool = ..., random_state: int = ..., remove=..., download_if_missing: bool = ..., return_X_y: bool = ...): ...
def fetch_20newsgroups_vectorized(*, subset: str = ..., remove=..., data_home: Any | None = ..., download_if_missing: bool = ..., return_X_y: bool = ..., normalize: bool = ..., as_frame: bool = ...): ...
