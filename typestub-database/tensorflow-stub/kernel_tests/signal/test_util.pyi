from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.lite.python import interpreter as interpreter, lite as lite
from tensorflow.python.eager import def_function as def_function
from tensorflow.python.grappler import tf_optimizer as tf_optimizer
from tensorflow.python.training import saver as saver
from typing import Any

def grappler_optimize(graph, fetches: Any | None = ..., config_proto: Any | None = ...): ...
def tflite_convert(fn, input_templates): ...
def evaluate_tflite_model(tflite_model, input_ndarrays): ...
