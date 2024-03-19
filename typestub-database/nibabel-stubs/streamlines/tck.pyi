from _typeshed import Incomplete
from nibabel.openers import Opener as Opener

from .array_sequence import ArraySequence as ArraySequence
from .header import Field as Field
from .tractogram import LazyTractogram as LazyTractogram
from .tractogram import Tractogram as Tractogram
from .tractogram import TractogramItem as TractogramItem
from .tractogram_file import DataError as DataError
from .tractogram_file import DataWarning as DataWarning
from .tractogram_file import HeaderError as HeaderError
from .tractogram_file import HeaderWarning as HeaderWarning
from .tractogram_file import TractogramFile as TractogramFile
from .utils import peek_next as peek_next

MEGABYTE: Incomplete

class TckFile(TractogramFile):
    MAGIC_NUMBER: bytes
    SUPPORTS_DATA_PER_POINT: bool
    SUPPORTS_DATA_PER_STREAMLINE: bool
    FIBER_DELIMITER: Incomplete
    EOF_DELIMITER: Incomplete
    def __init__(self, tractogram, header: Incomplete | None = None) -> None: ...
    @classmethod
    def is_correct_format(cls, fileobj): ...
    @classmethod
    def create_empty_header(cls): ...
    @classmethod
    def load(cls, fileobj, lazy_load: bool = False): ...
    def save(self, fileobj) -> None: ...
