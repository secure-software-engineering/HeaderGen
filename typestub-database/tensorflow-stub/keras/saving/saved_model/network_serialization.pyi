from tensorflow.python.keras.saving.saved_model import constants as constants, model_serialization as model_serialization

class NetworkSavedModelSaver(model_serialization.ModelSavedModelSaver):
    @property
    def object_identifier(self): ...
