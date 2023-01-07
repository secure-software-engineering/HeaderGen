from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.framework import errors as errors
from typing import Any

class _NotOkStatusException(Exception):
    message: Any
    code: Any
    payloads: Any
    def __init__(self, message, code, payloads) -> None: ...

class _FallbackException(Exception): ...
class _SymbolicException(Exception): ...
