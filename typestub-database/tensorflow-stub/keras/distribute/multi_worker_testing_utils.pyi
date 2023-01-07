from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python import keras as keras
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.distribute.cluster_resolver import SimpleClusterResolver as SimpleClusterResolver
from tensorflow.python.framework import dtypes as dtypes, errors as errors
from tensorflow.python.keras.optimizer_v2 import gradient_descent as gradient_descent
from tensorflow.python.ops import array_ops as array_ops, random_ops as random_ops
from tensorflow.python.training import server_lib as server_lib
from tensorflow.python.training.server_lib import ClusterSpec as ClusterSpec
from typing import Any

ASSIGNED_PORTS: Any
lock: Any

def mnist_synthetic_dataset(batch_size, steps_per_epoch): ...
def get_mnist_model(input_shape): ...
def make_parameter_server_cluster(num_workers, num_ps): ...
def pick_unused_port(): ...
def create_in_process_cluster(num_workers, num_ps, has_chief: bool = ..., has_eval: bool = ..., rpc_layer: str = ...): ...
