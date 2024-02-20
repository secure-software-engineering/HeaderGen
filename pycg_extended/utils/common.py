#
# Copyright (c) 2020 Vitalis Salis.
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
import os
import re
from pathlib import Path

import jupytext


def get_lambda_name(counter):
    return "<lambda{}>".format(counter)


def get_dict_name(counter):
    return "<dict{}>".format(counter)


def get_list_name(counter):
    return "<list{}>".format(counter)


def get_int_name(counter):
    return "<int{}>".format(counter)


def join_ns(*args):
    return ".".join([arg for arg in args])


def to_mod_name(name, package=None):
    return os.path.splitext(name)[0].replace("/", ".")


# This function quotes ipynb (notebook) specific symbols, such as "%" or "!"
# TODO: Improve regexp for all possible crashing symbols
def read_input_file(filename):
    file_content = ""
    py_ntbk_path = None
    if filename.endswith(".ipynb"):
        _file = Path(filename)
        _filename = _file.name.split(".ipynb")[0]
        ntbk = jupytext.read(_file)
        # py_ntbk = jupytext.writes(ntbk, fmt='py:percent')
        py_ntbk_path = "{}/{}-hg-analysis.py".format(Path(_file).parent, _filename)

        # write to python file for analysis
        jupytext.write(ntbk, py_ntbk_path, fmt="py:percent")
        filename = py_ntbk_path

    with open(filename, "rt") as f:
        for line in f:
            if re.search(r"^%|^\s%", line):  # searches line with the % symbol
                line = "#" + line
            if re.search(r"^!|^\s!", line):  # searches line with the ! symbol
                line = "#" + line
            file_content = file_content + line

    if py_ntbk_path:
        os.remove(py_ntbk_path)
    return file_content


def remove_obj_lineno(call_sites):
    output = {}
    for _cs_line, _cs_calls in call_sites.items():
        if _cs_line not in output:
            output[_cs_line] = set()
        for i in range(len(_cs_calls)):
            output[_cs_line].add(re.sub(r"<\d+>", "", _cs_calls[i]))

    return output


def remove_obj_lineno_cg(call_graph):
    output = {}
    for _cs_line, _cs_calls in call_graph.items():
        if _cs_line not in output:
            output[re.sub(r":\d+", "", _cs_line)] = set()
        for i in range(len(_cs_calls)):
            output[re.sub(r":\d+", "", _cs_line)].add(re.sub(r":\d+", "", _cs_calls[i]))

    return output


def remove_all_lineno(call_graph):
    pattern = re.compile(r":\d+")
    output = {}
    for _cs_line, _cs_calls in call_graph.items():
        if _cs_line not in output:
            output[pattern.sub("", _cs_line)] = set()
        for i in range(len(_cs_calls)):
            output[pattern.sub("", _cs_line)].add(pattern.sub("", _cs_calls[i]))

    return output


# %%
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


def is_int_str(string):
    return (string.startswith(("-", "+")) and string[1:].isdigit()) or string.isdigit()


def get_ns_without_last_lineno(ns):
    return re.sub(r"(?s)(?!:.*?(?=\.)):.*?(?=$)", "", ns)


def get_ns_without_obj_lineno(ns):
    return re.sub(r"<\d+>", "", ns)


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
            else re.sub(r"(?s)(?<=:).*?(?=\.)|(?<=:).*?(?=$)", cellid_repl, _call)
            for _call in _cs_calls
        ]

        for i in range(len(cell_calls)):
            cell_calls[i] = re.sub(r"<\d+>$", "", cell_calls[i])
        # _call = re.sub(r"<\d+>$", cellid_repl, _call)

        cell_call_sites[_cell_id] = cell_call_sites[_cell_id].union(cell_calls)

    return cell_call_sites


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
