from tensorflow.python.framework import errors as errors
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def trace(service_addr, logdir, duration_ms, worker_list: str = ..., num_tracing_attempts: int = ..., options: Any | None = ...) -> None: ...
def monitor(service_addr, duration_ms, level: int = ...): ...
