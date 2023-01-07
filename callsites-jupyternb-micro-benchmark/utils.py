import jupytext
import re
from pathlib import Path


def create_input_py(filename):
    py_ntbk_path = None
    if filename.endswith(".ipynb"):
        _file = Path(filename) 
        _filename = _file.name.split(".ipynb")[0]
        ntbk = jupytext.read(_file)
        # py_ntbk = jupytext.writes(ntbk, fmt='py:percent')
        py_ntbk_path = "{}/{}.py".format(Path(_file).parent, _filename)

        # write to python file for analysis
        jupytext.write(ntbk, py_ntbk_path, fmt='py:percent')
        filename = py_ntbk_path

    return filename


# Find all blocks and the line numbers in notebook script
def find_block_numbers(filename):
    if filename.endswith(".ipynb"):
        _file = Path(filename) 
        _filename = _file.name.split(".ipynb")[0]
        ntbk = jupytext.read(_file)
        py_ntbk = jupytext.writes(ntbk, fmt='py:percent')
        py_source_split = py_ntbk.split("\n")
    else:
        py_source_split = filename.split("\n")

    _start, _end = None, None
    lineno = 1
    block = 1
    mapping = {}

    _current_md = False
    for _line in py_source_split:
        if _line.startswith("# %%"):
            if _start is None:
                _start = lineno
                if _line.startswith("# %% [markdown]"):
                    _current_md = True
                else:
                    _current_md = False
            else:
                _end = lineno
                if _end == (_start+1):
                    _start = lineno
                    continue

                if not _current_md:
                    mapping[block] = {
                        "start": _start,
                        "end": _end - 1
                    }
                    block += 1

                _start = _end
                if _line.startswith("# %% [markdown]"):
                    _current_md = True
                else:
                    _current_md = False

        lineno += 1

    if not _current_md:    
        mapping[block] = {
            "start": _start,
            "end": lineno - 1
        }
    return mapping


def get_block_of_lineno(lineno, block_mapping):
    for map_key, map_value in block_mapping.items():
        if map_value["start"] <= lineno <= map_value["end"]:
            return map_key

    return None

def get_cell_numbers(call_sites, filename, module_name):
    block_mapping = find_block_numbers(filename)
    cell_call_sites = {}
    def cellid_repl(matchobj):
        _cell_id = get_block_of_lineno(int(matchobj.group(0)), block_mapping)
        return str(_cell_id)

    for _cs_line, _cs_calls in call_sites.items():
        # (:[\s\S]*?\.)|:[\s\S]*?$
        # :(.*)\.|:(.*)$
        _cell_id = get_block_of_lineno(int(_cs_line), block_mapping)
        if _cell_id not in cell_call_sites:
            cell_call_sites[_cell_id] = set()

        # only keep cellid of calls found in the same notebook
        cell_calls = [re.sub(r"(?s):.*?(?=\.)|:.*?(?=$)", "", _call) if not _call.startswith(module_name) 
                            else re.sub(r"(?s)(?<=:).*?(?=\.)|(?<=:).*?(?=$)", cellid_repl, _call) for _call in _cs_calls]

        cell_call_sites[_cell_id] = cell_call_sites[_cell_id].union(cell_calls)

    return cell_call_sites