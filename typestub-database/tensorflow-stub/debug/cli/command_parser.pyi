from typing import Any

class Interval:
    start: Any
    start_included: Any
    end: Any
    end_included: Any
    def __init__(self, start, start_included, end, end_included) -> None: ...
    def contains(self, value): ...
    def __eq__(self, other): ...

def parse_command(command): ...
def extract_output_file_path(args): ...
def parse_tensor_name_with_slicing(in_str): ...
def validate_slicing_string(slicing_string): ...
def parse_indices(indices_string): ...
def parse_ranges(range_string): ...
def parse_memory_interval(interval_str): ...
def parse_time_interval(interval_str): ...
def parse_readable_size_str(size_str): ...
def parse_readable_time_str(time_str): ...
def evaluate_tensor_slice(tensor, tensor_slicing): ...
def get_print_tensor_argparser(description): ...
