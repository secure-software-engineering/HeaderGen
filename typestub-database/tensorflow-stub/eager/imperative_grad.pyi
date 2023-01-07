from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.ops.unconnected_gradients import UnconnectedGradients as UnconnectedGradients
from tensorflow.python.util import compat as compat
from typing import Any, NamedTuple

class VSpace(NamedTuple):
    aggregate_fn: Any
    num_elements_fn: Any
    zeros_fn: Any
    ones_fn: Any
    zeros_like_fn: Any
    ones_like_fn: Any
    graph_shape_fn: Any

def imperative_grad(tape, target, sources, output_gradients: Any | None = ..., sources_raw: Any | None = ..., unconnected_gradients=...): ...
