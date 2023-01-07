from tensorflow.python.util import tf_export as tf_export
from typing import Any

class DocSource:
    docstring: Any
    docstring_module_name: Any
    def __init__(self, docstring: Any | None = ..., docstring_module_name: Any | None = ...) -> None: ...

def get_doc_sources(api_name): ...
