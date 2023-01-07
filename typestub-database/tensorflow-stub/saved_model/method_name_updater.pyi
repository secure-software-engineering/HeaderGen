from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.saved_model import constants as constants
from tensorflow.python.util import compat as compat
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class MethodNameUpdater:
    def __init__(self, export_dir) -> None: ...
    def replace_method_name(self, signature_key, method_name, tags: Any | None = ...) -> None: ...
    def save(self, new_export_dir: Any | None = ...) -> None: ...
