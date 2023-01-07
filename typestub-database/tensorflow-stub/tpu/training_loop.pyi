from tensorflow.python.compiler.xla import xla as xla
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops
from tensorflow.python.tpu import tensor_tracer as tensor_tracer, tpu_feed as tpu_feed, tpu_function as tpu_function
from tensorflow.python.types import core as core_types
from typing import Any, Callable, Iterable, List, Optional, Union

def while_loop(condition: Callable[..., Any], body: Callable[..., Any], inputs: Optional[List[Any]] = ..., infeed_queue: Optional[tpu_feed.InfeedQueue] = ..., name: Any = ...) -> Any: ...
def repeat(n: int, body: Callable[..., Union[core_types.TensorLike, Iterable]], inputs: Optional[List[core_types.TensorLike]] = ..., infeed_queue: Optional[tpu_feed.InfeedQueue] = ..., name: Any = ...) -> List[core_types.TensorLike]: ...
