import re
from pathlib import Path

import jupytext


def remove_element(element, the_list):
    the_list = list(set(the_list))
    the_list.remove(element)
    return the_list


def create_input_py(filename):
    py_ntbk_path = None
    if filename.endswith(".ipynb"):
        _file = Path(filename)
        _filename = _file.name.split(".ipynb")[0]
        ntbk = jupytext.read(_file)
        # py_ntbk = jupytext.writes(ntbk, fmt='py:percent')
        py_ntbk_path = "{}/{}.py".format(Path(_file).parent, _filename)

        # write to python file for analysis
        jupytext.write(ntbk, py_ntbk_path, fmt="py:percent")
        filename = py_ntbk_path

    return filename


# Find all blocks and the line numbers in notebook script
def find_block_numbers(filename):
    if filename.endswith(".ipynb"):
        _file = Path(filename)
        _filename = _file.name.split(".ipynb")[0]
        ntbk = jupytext.read(_file)
        py_ntbk = jupytext.writes(ntbk, fmt="py:percent")
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
                if _end == (_start + 1):
                    _start = lineno
                    continue

                if not _current_md:
                    mapping[block] = {"start": _start, "end": _end - 1}
                    block += 1

                _start = _end
                if _line.startswith("# %% [markdown]"):
                    _current_md = True
                else:
                    _current_md = False

        lineno += 1

    if not _current_md:
        mapping[block] = {"start": _start, "end": lineno - 1}
    return mapping


def get_block_of_lineno(lineno, block_mapping):
    for map_key, map_value in block_mapping.items():
        if map_value["start"] <= lineno <= map_value["end"]:
            return map_key

    return None


def get_clear_lineno(call_str):
    return re.sub(r"<\d+>", "", call_str)


def get_clear_all_lineno(call_str):
    return re.sub(r"(?s):.*?(?=\.)|:.*?(?=$)", "", call_str)


def dot_to_bracket_notation(code_str):
    # find the dot notations in the string and replace them
    return re.sub(
        r"\b([^.\s]+(\.[^.\s]+)+)\b",
        lambda m: m.group(1).split(".")[0]
        + "['"
        + "']['".join(m.group(1).split(".")[1:])
        + "']",
        code_str,
    )


def replace_dict_int_keys(dict_key):
    return re.sub("<int([0-9].*)>$", r"\1", dict_key)


def get_list_int(s):
    match = re.search(r"(\d+)[^0-9]*$", s)
    if match:
        return int(match.group(1))
    return None


def ends_with_dict(name):
    match = re.search(r".*<dict([0-9]+)>$", name)

    if match is not None:
        return True

    return False


def is_dict(name, specific_dict=None):
    if specific_dict:
        pattern = f"<dict{specific_dict}>\.(.*)"
        match = re.search(pattern, name)
        if match is not None:
            return True
    else:
        match = re.search(r".*<dict([0-9]+)>$", name)

        if match is not None:
            number = match.group(1)
            return number

    return False


def is_list(name, specific_list=None):
    if specific_list:
        pattern = f"<list{specific_list}>\.(.*)"
        match = re.search(pattern, name)
        if match is not None:
            return True
    else:
        match = re.search(r".*<list([0-9]+)>$", name)

        if match is not None:
            number = match.group(1)
            return number

    return False


def is_local_in_scope(local, pycg_def):
    pattern = rf"\b{local}\b.*$"
    match = re.search(pattern, pycg_def)
    if match is not None:
        return True

    return False


def get_last_lineno_return(call_str):
    matches = re.findall(r":(\d+).<RETURN>", call_str)
    if matches:
        return matches[-1]

    # No lineno, therefor external funcdef
    return False


def get_line_numbers_cleaned(call_sites, filename, module_name):
    line_call_sites = {}

    def cellid_repl(matchobj):
        return str(int(matchobj.group(0)))

    for _cs_line, _cs_calls in call_sites.items():
        # (:[\s\S]*?\.)|:[\s\S]*?$
        # :(.*)\.|:(.*)$
        _cell_id = int(_cs_line)
        if _cell_id not in line_call_sites:
            line_call_sites[_cell_id] = set()

        # only keep cellid of calls found in the same notebook
        cell_calls = [
            re.sub(r"(?s):.*?(?=\.)|:.*?(?=$)", "", _call)
            if not _call.startswith(module_name)
            else re.sub(
                r"(?s)(?<=:).*?(?=\.)|(?<=:).*?(?=$)",
                cellid_repl,
                _call.replace("-hg-analysis", ""),
            )
            for _call in _cs_calls
        ]

        for i in range(len(cell_calls)):
            cell_calls[i] = re.sub(r"<\d+>", "", cell_calls[i])
        # _call = re.sub(r"<\d+>$", cellid_repl, _call)

        line_call_sites[_cell_id] = line_call_sites[_cell_id].union(cell_calls)

    return line_call_sites


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
        cell_calls = [
            re.sub(r"(?s):.*?(?=\.)|:.*?(?=$)", "", _call)
            if not _call.startswith(module_name)
            else re.sub(
                r"(?s)(?<=:).*?(?=\.)|(?<=:).*?(?=$)",
                cellid_repl,
                _call.replace("-hg-analysis", ""),
            )
            for _call in _cs_calls
        ]

        for i in range(len(cell_calls)):
            cell_calls[i] = re.sub(r"<\d+>", "", cell_calls[i])
        # _call = re.sub(r"<\d+>$", cellid_repl, _call)

        cell_call_sites[_cell_id] = cell_call_sites[_cell_id].union(cell_calls)

    return cell_call_sites
