from keras.saving.saved_model import constants as constants, layer_serialization as layer_serialization
from keras.utils import generic_utils as generic_utils

class MetricSavedModelSaver(layer_serialization.LayerSavedModelSaver):
    @property
    def object_identifier(self): ...
