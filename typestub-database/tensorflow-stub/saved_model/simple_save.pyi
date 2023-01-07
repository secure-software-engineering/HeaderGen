from tensorflow.python.framework import ops as ops
from tensorflow.python.saved_model import builder as builder, signature_constants as signature_constants, signature_def_utils as signature_def_utils, tag_constants as tag_constants
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def simple_save(session, export_dir, inputs, outputs, legacy_init_op: Any | None = ...) -> None: ...
