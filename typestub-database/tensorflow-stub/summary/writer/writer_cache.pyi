from tensorflow.python.framework import ops as ops
from tensorflow.python.summary.writer.writer import FileWriter as FileWriter
from tensorflow.python.util.tf_export import tf_export as tf_export

class FileWriterCache:
    @staticmethod
    def clear() -> None: ...
    @staticmethod
    def get(logdir): ...
