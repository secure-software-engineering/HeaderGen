from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

class _BlockLSTMOutput(NamedTuple):
    i: Any
    cs: Any
    f: Any
    o: Any
    ci: Any
    co: Any
    h: Any

def block_lstm(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, forget_bias: int = ..., cell_clip: int = ..., use_peephole: bool = ..., name: Any | None = ...): ...

BlockLSTM: Any

def block_lstm_eager_fallback(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, forget_bias, cell_clip, use_peephole, name, ctx): ...

class _BlockLSTMGradOutput(NamedTuple):
    x_grad: Any
    cs_prev_grad: Any
    h_prev_grad: Any
    w_grad: Any
    wci_grad: Any
    wcf_grad: Any
    wco_grad: Any
    b_grad: Any

def block_lstm_grad(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, i, cs, f, o, ci, co, h, cs_grad, h_grad, use_peephole, name: Any | None = ...): ...

BlockLSTMGrad: Any

def block_lstm_grad_eager_fallback(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, i, cs, f, o, ci, co, h, cs_grad, h_grad, use_peephole, name, ctx): ...

class _BlockLSTMGradV2Output(NamedTuple):
    x_grad: Any
    cs_prev_grad: Any
    h_prev_grad: Any
    w_grad: Any
    wci_grad: Any
    wcf_grad: Any
    wco_grad: Any
    b_grad: Any

def block_lstm_grad_v2(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, i, cs, f, o, ci, co, h, cs_grad, h_grad, use_peephole, name: Any | None = ...): ...

BlockLSTMGradV2: Any

def block_lstm_grad_v2_eager_fallback(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, i, cs, f, o, ci, co, h, cs_grad, h_grad, use_peephole, name, ctx): ...

class _BlockLSTMV2Output(NamedTuple):
    i: Any
    cs: Any
    f: Any
    o: Any
    ci: Any
    co: Any
    h: Any

def block_lstmv2(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, cell_clip: int = ..., use_peephole: bool = ..., name: Any | None = ...): ...

BlockLSTMV2: Any

def block_lstmv2_eager_fallback(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, cell_clip, use_peephole, name, ctx): ...

class _GRUBlockCellOutput(NamedTuple):
    r: Any
    u: Any
    c: Any
    h: Any

def gru_block_cell(x, h_prev, w_ru, w_c, b_ru, b_c, name: Any | None = ...): ...

GRUBlockCell: Any

def gru_block_cell_eager_fallback(x, h_prev, w_ru, w_c, b_ru, b_c, name, ctx): ...

class _GRUBlockCellGradOutput(NamedTuple):
    d_x: Any
    d_h_prev: Any
    d_c_bar: Any
    d_r_bar_u_bar: Any

def gru_block_cell_grad(x, h_prev, w_ru, w_c, b_ru, b_c, r, u, c, d_h, name: Any | None = ...): ...

GRUBlockCellGrad: Any

def gru_block_cell_grad_eager_fallback(x, h_prev, w_ru, w_c, b_ru, b_c, r, u, c, d_h, name, ctx): ...

class _LSTMBlockCellOutput(NamedTuple):
    i: Any
    cs: Any
    f: Any
    o: Any
    ci: Any
    co: Any
    h: Any

def lstm_block_cell(x, cs_prev, h_prev, w, wci, wcf, wco, b, forget_bias: int = ..., cell_clip: int = ..., use_peephole: bool = ..., name: Any | None = ...): ...

LSTMBlockCell: Any

def lstm_block_cell_eager_fallback(x, cs_prev, h_prev, w, wci, wcf, wco, b, forget_bias, cell_clip, use_peephole, name, ctx): ...

class _LSTMBlockCellGradOutput(NamedTuple):
    cs_prev_grad: Any
    dicfo: Any
    wci_grad: Any
    wcf_grad: Any
    wco_grad: Any

def lstm_block_cell_grad(x, cs_prev, h_prev, w, wci, wcf, wco, b, i, cs, f, o, ci, co, cs_grad, h_grad, use_peephole, name: Any | None = ...): ...

LSTMBlockCellGrad: Any

def lstm_block_cell_grad_eager_fallback(x, cs_prev, h_prev, w, wci, wcf, wco, b, i, cs, f, o, ci, co, cs_grad, h_grad, use_peephole, name, ctx): ...
