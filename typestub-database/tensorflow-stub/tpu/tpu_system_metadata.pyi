from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.distribute import device_util as device_util
from tensorflow.python.eager import context as context
from tensorflow.python.framework import config as config, errors as errors, ops as ops
from tensorflow.python.tpu import tpu as tpu
from tensorflow.python.util.tf_export import tf_export as tf_export

class TPUSystemMetadata:
    def __new__(cls, num_cores, num_hosts, num_of_cores_per_host, topology, devices): ...

def get_session_config_with_timeout(timeout_in_secs, cluster_def): ...
def master_job(master, cluster_def): ...
