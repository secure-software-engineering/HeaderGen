from tensorflow.core.protobuf import graph_debug_info_pb2 as graph_debug_info_pb2
from typing import Any, NamedTuple

class _ParseTag(NamedTuple):
    type: Any
    name: Any

def parse_message(message): ...
def create_graph_debug_info_def(func_named_operations): ...
def interpolate(error_message, graph): ...
