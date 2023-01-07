from tensorflow.python.client._pywrap_tf_session import *
from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow
from typing import Any

__git_version__: Any
__compiler_version__: Any
__cxx11_abi_flag__: Any
__monolithic_build__: Any
GRAPH_DEF_VERSION: Any
GRAPH_DEF_VERSION_MIN_CONSUMER: Any
GRAPH_DEF_VERSION_MIN_PRODUCER: Any
TENSOR_HANDLE_KEY: Any

def TF_NewSessionOptions(target: Any | None = ..., config: Any | None = ...): ...
def TF_Reset(target, containers: Any | None = ..., config: Any | None = ...) -> None: ...
