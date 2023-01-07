from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

class _BatchOutput(NamedTuple):
    batched_tensors: Any
    batch_index: Any
    id: Any

def batch(in_tensors, num_batch_threads, max_batch_size, batch_timeout_micros, grad_timeout_micros, max_enqueued_batches: int = ..., allowed_batch_sizes=..., container: str = ..., shared_name: str = ..., batching_queue: str = ..., name: Any | None = ...): ...

Batch: Any

def batch_eager_fallback(in_tensors, num_batch_threads, max_batch_size, batch_timeout_micros, grad_timeout_micros, max_enqueued_batches, allowed_batch_sizes, container, shared_name, batching_queue, name, ctx): ...
def batch_function(in_tensors, captured_tensors, f, num_batch_threads, max_batch_size, batch_timeout_micros, Tout, max_enqueued_batches: int = ..., allowed_batch_sizes=..., container: str = ..., shared_name: str = ..., batching_queue: str = ..., enable_large_batch_splitting: bool = ..., name: Any | None = ...): ...

BatchFunction: Any

def batch_function_eager_fallback(in_tensors, captured_tensors, f, num_batch_threads, max_batch_size, batch_timeout_micros, Tout, max_enqueued_batches, allowed_batch_sizes, container, shared_name, batching_queue, enable_large_batch_splitting, name, ctx): ...
def unbatch(batched_tensor, batch_index, id, timeout_micros, container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

Unbatch: Any

def unbatch_eager_fallback(batched_tensor, batch_index, id, timeout_micros, container, shared_name, name, ctx): ...
def unbatch_grad(original_input, batch_index, grad, id, container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

UnbatchGrad: Any

def unbatch_grad_eager_fallback(original_input, batch_index, grad, id, container, shared_name, name, ctx): ...
