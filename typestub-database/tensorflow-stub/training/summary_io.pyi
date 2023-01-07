from tensorflow.python.summary.summary_iterator import summary_iterator as summary_iterator
from tensorflow.python.summary.writer.writer import FileWriter as _FileWriter
from tensorflow.python.util.deprecation import deprecated as deprecated
from typing import Any

class SummaryWriter(_FileWriter):
    def __init__(self, logdir, graph: Any | None = ..., max_queue: int = ..., flush_secs: int = ..., graph_def: Any | None = ...) -> None: ...
