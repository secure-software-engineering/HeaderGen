from tensorflow.python.keras.saving.saved_model import constants as constants, layer_serialization as layer_serialization
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.training.tracking import data_structures as data_structures

class MetricSavedModelSaver(layer_serialization.LayerSavedModelSaver):
    @property
    def object_identifier(self): ...
