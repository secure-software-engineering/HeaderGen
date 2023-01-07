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
import sys
import importlib
import json
import utils

from unittest import TestCase, main


class TestBase(TestCase):
    snippet_dir = ""

    def setUp(self):
        def error():
            print("Invalid module %s.%s" % (cg_mod, cg_class))
            print(
                "Set environment variables `CALL_GRAPH_CLASS` and `CALL_GRAPH_MODULE` properly"
            )
            sys.exit(1)

        self.snippets_path = os.environ.get("SNIPPETS_PATH")
        self.notebooks_path = os.environ.get("NOTEBOOKS_PATH")
        cg_class = "CallGraphGenerator"
        cg_mod = "pycg_extended.pycg"
        if not cg_class or not cg_mod:
            error()
        try:
            self.cg_mod = importlib.import_module(cg_mod)
        except ImportError:
            error()

        self.cg_class = getattr(self.cg_mod, cg_class)
        if not self.cg_class:
            error()

    def validate_snippet(self, snippet_path):
        output = self.get_snippet_output_cs(snippet_path)
        expected = self.get_snippet_expected_cs(snippet_path)

        def do_sorted(d):
            s = {}
            for n in d:
                s[str(n)] = sorted(d[n])
            return s

        self.assertEqual(output, expected)

    def get_snippet_path(self, name):
        return os.path.join(self.snippets_path, self.snippet_dir, name)

    def get_snippet_output_cg(self, snippet_path):
        main_path = os.path.join(snippet_path, "main.py")
        try:
            cg = self.cg_class([main_path], snippet_path, -1, "call-graph")
            cg.analyze()
            return cg.output()
        except Exception as e:
            cg.tearDown()
            raise e

    def get_snippet_output_cs(self, snippet_path):
        main_path = os.path.join(snippet_path, "main.py")
        try:
            cs = self.cg_class([main_path], snippet_path, -1, "call-site")
            cs.analyze()
            # graphs = self.get_json_graph(cs)
            return cs.output_call_sites(module_name="main")
        except Exception as e:
            cs.tearDown()
            raise e

    def validate_notebook(self, snippet_path):
        output = self.get_notebook_output_cs(snippet_path)
        expected = self.get_notebook_expected_cs(snippet_path)

        self.assertEqual(output, expected)

    def get_notebook_expected_cs(self, snippet_path):
        cg_path = os.path.join(snippet_path, "cellsCallSite.json")
        with open(cg_path, "r") as f:
            return json.loads(f.read())

    def get_notebook_output_cs(self, snippet_path):
        main_nb_path = os.path.join(snippet_path, "main_nb.ipynb")
        # TODO: notebook conversion should be part of pycg
        main_path = utils.create_input_py(main_nb_path)
        try:
            cs = self.cg_class([main_path], snippet_path, -1, "call-site")
            cs.analyze()
            output_callsites = cs.output_call_sites(module_name="main_nb")

            return utils.get_cell_numbers(
                output_callsites, main_nb_path, module_name="main_nb"
            )
        except Exception as e:
            cs.tearDown()
            raise e
        finally:
            os.remove(main_path)

    def get_json_graph(self, cg):
        from pycg_extended import formats
        from collections import OrderedDict

        formatter = formats.Simple(cg)
        as_formatter = formats.AsGraph(cg)

        fa_formatter = formats.Fasten(cg, None, "", "", "", 0)

        cs_formatter = formats.CallSites(cg)

        cg_json = formatter.generate()
        ag_json = as_formatter.generate()
        fa_json = fa_formatter.generate()

        cs_json = cs_formatter.generate()
        cs_json = cs_formatter.get_cg()
        # cs_json = cs_formatter.get_ag()

        return (
            OrderedDict(sorted(cg_json.items())),
            OrderedDict(sorted(ag_json.items())),
        )

    def get_snippet_expected_cg(self, snippet_path):
        cg_path = os.path.join(snippet_path, "callgraph.json")
        with open(cg_path, "r") as f:
            return json.loads(f.read())

    def get_snippet_expected_cs(self, snippet_path):
        cg_path = os.path.join(snippet_path, "linesCallSite.json")
        with open(cg_path, "r") as f:
            return json.loads(f.read())

    def assertEqual(self, actual, expected):
        def do_sorted(d):
            s = {}
            for n in d:
                s[str(n)] = sorted(d[n])
            return s

        super().assertEqual(do_sorted(actual), do_sorted(expected))


if __name__ == "__main__":
    main()
