from tensorflow.core.protobuf import saved_model_pb2 as saved_model_pb2
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.saved_model import constants as constants
from tensorflow.python.util import compat as compat

def read_saved_model(saved_model_dir): ...
def get_saved_model_tag_sets(saved_model_dir): ...
def get_meta_graph_def(saved_model_dir, tag_set): ...
