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
from .base import BaseFormatter
from collections import OrderedDict
from pycg_extended import utils


class CallSites(BaseFormatter):
    def __init__(self, cg_generator):
        self.cg_generator = cg_generator

    def generate(self, module_name):
        output = self.cg_generator.output_call_sites(module_name)
        output = utils.remove_obj_lineno(output)
        return OrderedDict(sorted(output.items()))

    # HACK: Should be from csprocessor / pycg.py. not here
    def get_cg(self):
        output = self.cg_generator.cs.get()
        output_cg = {}
        for node in output:
            output_cg[node] = list(output[node])
        output_cg = utils.remove_obj_lineno_cg(output_cg)
        return output_cg

    def get_imports(self):
        output = self.cg_generator.import_manager.get_import_graph()
        return output
