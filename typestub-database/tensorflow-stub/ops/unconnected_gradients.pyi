import enum
from tensorflow.python.util.tf_export import tf_export as tf_export

class UnconnectedGradients(enum.Enum):
    NONE: str
    ZERO: str
