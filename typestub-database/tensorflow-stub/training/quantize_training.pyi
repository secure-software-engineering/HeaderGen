from tensorflow.core.framework import graph_pb2 as graph_pb2
from tensorflow.python._pywrap_quantize_training import DoQuantizeTrainingOnGraphDefHelper as DoQuantizeTrainingOnGraphDefHelper
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

def do_quantize_training_on_graphdef(input_graph, num_bits): ...
