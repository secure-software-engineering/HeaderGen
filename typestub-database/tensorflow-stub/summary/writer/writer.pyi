from tensorflow.core.framework import graph_pb2 as graph_pb2, summary_pb2 as summary_pb2
from tensorflow.core.protobuf import meta_graph_pb2 as meta_graph_pb2
from tensorflow.core.util import event_pb2 as event_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import meta_graph as meta_graph, ops as ops
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.summary import plugin_asset as plugin_asset
from tensorflow.python.summary.writer.event_file_writer import EventFileWriter as EventFileWriter
from tensorflow.python.summary.writer.event_file_writer_v2 import EventFileWriterV2 as EventFileWriterV2
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class SummaryToEventTransformer:
    event_writer: Any
    def __init__(self, event_writer, graph: Any | None = ..., graph_def: Any | None = ...) -> None: ...
    def add_summary(self, summary, global_step: Any | None = ...) -> None: ...
    def add_session_log(self, session_log, global_step: Any | None = ...) -> None: ...
    def add_graph(self, graph, global_step: Any | None = ..., graph_def: Any | None = ...) -> None: ...
    def add_meta_graph(self, meta_graph_def, global_step: Any | None = ...) -> None: ...
    def add_run_metadata(self, run_metadata, tag, global_step: Any | None = ...) -> None: ...

class FileWriter(SummaryToEventTransformer):
    def __init__(self, logdir, graph: Any | None = ..., max_queue: int = ..., flush_secs: int = ..., graph_def: Any | None = ..., filename_suffix: Any | None = ..., session: Any | None = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, unused_type, unused_value, unused_traceback) -> None: ...
    def get_logdir(self): ...
    def add_event(self, event) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...
    def reopen(self) -> None: ...
