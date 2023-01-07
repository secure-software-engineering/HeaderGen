from tensorflow.core.framework import graph_pb2 as graph_pb2
from tensorflow.core.protobuf import config_pb2 as config_pb2
from typing import Any

def OptimizeGraph(config_proto, metagraph, verbose: bool = ..., graph_id: bytes = ..., cluster: Any | None = ..., strip_default_attributes: bool = ...): ...
