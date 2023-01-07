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
from collections import namedtuple

Node = namedtuple("Node", ["src", "dest"])


class CallSites(object):
    def __init__(self):
        self.cg = {}
        self.modnames = {}
        self.callsites = {}
        # NOTE: Flow Sensitive
        # self.usedef_info = {}
        # self.assignment_graph = None

    # NOTE: Flow Sensitive
    # def add_usedef_info(self, modname, usedefinfo, assignment_graph):
    #     self.usedef_info[modname] = usedefinfo
    #     self.assignment_graph = assignment_graph

    def add_node(self, name, modname=""):
        if not isinstance(name, str):
            raise CallSiteError("Only string node names allowed")
        if not name:
            raise CallSiteError("Empty node name")

        if not name in self.cg:
            self.cg[name] = set()
            self.modnames[name] = modname
            # print("Node:", modname, "--", name)
            # print("CG:", self.cg)
            # print("MOD:", self.modnames)

        if name in self.cg and not self.modnames[name]:
            self.modnames[name] = modname
            # print("NMOD:", self.modnames)

    def add_edge(self, src, dest, node):
        # print("\nEdge:", src, "-->", dest)
        self.add_node(src)
        self.add_node(dest)
        self.cg[src].add(dest)
        # print("CG:", self.cg)
        # print("Edge: Done")

        # TODO: Should be lineno
        if hasattr(node, "lineno"):
            if dest not in self.callsites:
                self.callsites[dest] = set()

            self.callsites[dest].add(node.lineno)

    def get(self):
        return self.cg

    def get_edges(self):
        output = []
        for src in self.cg:
            for dst in self.cg[src]:
                output.append([src, dst])
        return output

    def get_modules(self):
        return self.modnames

    def get_call_sites_lineno(self, module_name=None):
        _call_sites_lineno = {}
        processed_calls = []

        def _get_leaf_nodes(_call):
            nonlocal module_name, processed_calls
            for _line in root_ln:
                if _line not in _call_sites_lineno:
                    _call_sites_lineno[_line] = []

                if _call not in _call_sites_lineno[_line]:
                    _call_sites_lineno[_line].append(_call)

            if len(self.cg[_call]) > 0:
                for _c in self.cg[_call]:
                    if _c not in processed_calls:
                        processed_calls.append(_c)
                        _get_leaf_nodes(_c)

        for _src, _dest in self.cg.items():
            if module_name is not None:
                # Analyze call-sites only in the main module
                if _src.split(".")[0] == module_name:
                    for _call in _dest:
                        root_ln = self.callsites[_call]
                        _get_leaf_nodes(_call)
                        processed_calls = []
            else:
                for _call in _dest:
                    root_ln = self.callsites[_call]
                    _get_leaf_nodes(_call)
                    processed_calls = []

        return _call_sites_lineno


class CallSiteError(Exception):
    pass
