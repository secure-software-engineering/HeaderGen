from patsy import NAAction
from typing import Any

formula_handler: Any

def handle_formula_data(Y, X, formula, depth: int = ..., missing: str = ...): ...
def make_hypotheses_matrices(model_results, test_formula): ...
