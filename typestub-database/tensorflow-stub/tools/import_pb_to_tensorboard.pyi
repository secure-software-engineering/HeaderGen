from tensorflow.contrib.tensorrt.ops.gen_trt_engine_op import *
from tensorflow.python.client import session as session
from tensorflow.python.framework import importer as importer, ops as ops
from tensorflow.python.summary import summary as summary
from tensorflow.python.tools import saved_model_utils as saved_model_utils

def import_to_tensorboard(model_dir, log_dir, tag_set) -> None: ...
def main(_) -> None: ...
