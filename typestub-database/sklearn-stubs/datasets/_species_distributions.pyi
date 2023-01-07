from . import get_data_home as get_data_home
from ..utils import Bunch as Bunch
from ._base import RemoteFileMetadata as RemoteFileMetadata
from typing import Any

SAMPLES: Any
COVERAGES: Any
DATA_ARCHIVE_NAME: str
logger: Any

def construct_grids(batch): ...
def fetch_species_distributions(*, data_home: Any | None = ..., download_if_missing: bool = ...): ...
