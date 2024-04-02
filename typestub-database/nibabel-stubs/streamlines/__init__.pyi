from _typeshed import Incomplete

from .array_sequence import ArraySequence as ArraySequence
from .header import Field as Field
from .tck import TckFile as TckFile
from .tractogram import LazyTractogram as LazyTractogram
from .tractogram import Tractogram as Tractogram
from .tractogram_file import ExtensionWarning as ExtensionWarning
from .trk import TrkFile as TrkFile

FORMATS: Incomplete

def is_supported(fileobj): ...
def detect_format(fileobj): ...
def load(fileobj, lazy_load: bool = False): ...
def save(tractogram, filename, **kwargs) -> None: ...
