from keras import testing_utils as testing_utils
from keras.distribute import keras_correctness_test_base as keras_correctness_test_base
from keras.mixed_precision import policy as policy
from typing import Any

class _DistributionStrategyRnnModelCorrectnessTest(keras_correctness_test_base.TestDistributionStrategyEmbeddingModelCorrectnessBase):
    def get_model(self, max_words: int = ..., initial_weights: Any | None = ..., distribution: Any | None = ..., input_shapes: Any | None = ...): ...

class DistributionStrategyGruModelCorrectnessTest(_DistributionStrategyRnnModelCorrectnessTest):
    def test_gru_model_correctness(self, distribution, use_numpy, use_validation_data) -> None: ...

class DistributionStrategyLstmModelCorrectnessTest(_DistributionStrategyRnnModelCorrectnessTest):
    def test_lstm_model_correctness(self, distribution, use_numpy, use_validation_data) -> None: ...
    def test_lstm_model_correctness_mixed_precision(self, distribution, use_numpy, use_validation_data) -> None: ...
