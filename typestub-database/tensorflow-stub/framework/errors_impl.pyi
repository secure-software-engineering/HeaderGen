from tensorflow.core.lib.core import error_codes_pb2 as error_codes_pb2
from tensorflow.python.framework import c_api_util as c_api_util
from tensorflow.python.util import compat as compat, deprecation as deprecation, tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class InaccessibleTensorError(ValueError): ...
class OperatorNotAllowedInGraphError(TypeError): ...

class OpError(Exception):
    def __init__(self, node_def, op, message, error_code, *args) -> None: ...
    def __reduce__(self): ...
    @property
    def message(self): ...
    @property
    def op(self): ...
    @property
    def error_code(self): ...
    @property
    def node_def(self): ...
    @property
    def experimental_payloads(self): ...

OK: Any
CANCELLED: Any
UNKNOWN: Any
INVALID_ARGUMENT: Any
DEADLINE_EXCEEDED: Any
NOT_FOUND: Any
ALREADY_EXISTS: Any
PERMISSION_DENIED: Any
UNAUTHENTICATED: Any
RESOURCE_EXHAUSTED: Any
FAILED_PRECONDITION: Any
ABORTED: Any
OUT_OF_RANGE: Any
UNIMPLEMENTED: Any
INTERNAL: Any
UNAVAILABLE: Any
DATA_LOSS: Any

class CancelledError(OpError):
    def __init__(self, node_def, op, message, *args) -> None: ...

class UnknownError(OpError):
    def __init__(self, node_def, op, message, *args) -> None: ...

class InvalidArgumentError(OpError):
    def __init__(self, node_def, op, message, *args) -> None: ...

class DeadlineExceededError(OpError):
    def __init__(self, node_def, op, message, *args) -> None: ...

class NotFoundError(OpError):
    def __init__(self, node_def, op, message, *args) -> None: ...

class AlreadyExistsError(OpError):
    def __init__(self, node_def, op, message, *args) -> None: ...

class PermissionDeniedError(OpError):
    def __init__(self, node_def, op, message, *args) -> None: ...

class UnauthenticatedError(OpError):
    def __init__(self, node_def, op, message, *args) -> None: ...

class ResourceExhaustedError(OpError):
    def __init__(self, node_def, op, message, *args) -> None: ...

class FailedPreconditionError(OpError):
    def __init__(self, node_def, op, message, *args) -> None: ...

class AbortedError(OpError):
    def __init__(self, node_def, op, message, *args) -> None: ...

class OutOfRangeError(OpError):
    def __init__(self, node_def, op, message, *args) -> None: ...

class UnimplementedError(OpError):
    def __init__(self, node_def, op, message, *args) -> None: ...

class InternalError(OpError):
    def __init__(self, node_def, op, message, *args) -> None: ...

class UnavailableError(OpError):
    def __init__(self, node_def, op, message, *args) -> None: ...

class DataLossError(OpError):
    def __init__(self, node_def, op, message, *args) -> None: ...

def exception_type_from_error_code(error_code): ...
def error_code_from_exception_type(cls): ...

class raise_exception_on_not_ok_status:
    status: Any
    def __enter__(self): ...
    def __exit__(self, type_arg, value_arg, traceback_arg): ...
