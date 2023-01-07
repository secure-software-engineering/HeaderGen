from tensorflow.python.lib.io.file_io import FileIO as _FileIO
from tensorflow.python.util.deprecation import deprecated as deprecated
from tensorflow.python.util.tf_export import tf_export as tf_export

class GFile(_FileIO):
    def __init__(self, name, mode: str = ...) -> None: ...

class FastGFile(_FileIO):
    def __init__(self, name, mode: str = ...) -> None: ...
Open = GFile
