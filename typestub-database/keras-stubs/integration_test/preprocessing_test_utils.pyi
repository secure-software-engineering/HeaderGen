from typing import Any

preprocessing: Any
BATCH_SIZE: int
DS_SIZE: Any
STEPS: Any
VOCAB_SIZE: int

def make_dataset(): ...
def make_preprocessing_model(file_dir): ...
def make_training_model(): ...
