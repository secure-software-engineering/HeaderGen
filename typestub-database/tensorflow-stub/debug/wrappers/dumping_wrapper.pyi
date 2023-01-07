from tensorflow.core.util import event_pb2 as event_pb2
from tensorflow.python.debug.lib import debug_data as debug_data
from tensorflow.python.debug.wrappers import framework as framework
from tensorflow.python.platform import gfile as gfile
from typing import Any

class DumpingDebugWrapperSession(framework.NonInteractiveDebugWrapperSession):
    def __init__(self, sess, session_root, watch_fn: Any | None = ..., thread_name_filter: Any | None = ..., pass_through_operrors: Any | None = ..., log_usage: bool = ...) -> None: ...
    def prepare_run_debug_urls(self, fetches, feed_dict): ...
