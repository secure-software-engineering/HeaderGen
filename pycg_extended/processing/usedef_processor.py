from beniget import beniget
import gast

# NOTE: Flow Sensitive


class UseDefProcessor(gast.NodeVisitor):
    use_def_cache = {}

    def __init__(self, module_path):
        self.module_path = module_path
        self.module_node = gast.parse(open(module_path).read())

        self.duc = beniget.DefUseChains()
        self.duc.visit(self.module_node)

        self.udc = beniget.UseDefChains(self.duc)

        if module_path not in UseDefProcessor.use_def_cache:
            self.analyze()
        else:
            self.line_uses = UseDefProcessor.use_def_cache[module_path]["line_uses"]
            self.locals_defs = UseDefProcessor.use_def_cache[module_path]["locals_defs"]

    def analyze(self):
        self.generic_visit(self.module_node)
        self.line_uses, self.locals_defs = self.get_all_definitions_for_use()
        UseDefProcessor.use_def_cache[self.module_path] = {
            "line_uses": self.line_uses,
            "locals_defs": self.locals_defs,
        }

    # def visit_Call(self, node):
    #     for _def in self.udc.chains[node]:
    #         _def
    #         for _def2 in self.udc.chains[_def.node]:
    #             _def2

    def get_all_definitions_for_use(self, full_nodes=False):
        node = self.module_node
        variable_defs = {}
        locals_defs = []
        # for _chain in self.duc.chains.values():
        #     print(_chain)
        # for _use in _chain.users():
        #     _use

        def _visit_child_locals(inner_node):
            inner_locals = self.duc.locals[inner_node]
            # inner_locals
            for _var in inner_locals:
                # for _use in self.duc.chains[_var.node].users():
                #     _use
                # print(_var)
                if isinstance(_var.node, gast.ClassDef) or isinstance(
                    _var.node, gast.FunctionDef
                ):
                    _id = _var.node.name + ":" + str(_var.node.lineno)
                    _visit_child_locals(_var.node)
                elif isinstance(_var.node, gast.Name):
                    _id = _var.node.id + ":" + str(_var.node.lineno)
                    locals_defs.append(_id)
                elif isinstance(_var.node, gast.alias):
                    if _var.node.asname:
                        _id = _var.node.asname
                    else:
                        _id = _var.node.name

                for _use in _var.users():
                    if not _use.node.lineno in variable_defs:
                        variable_defs[_use.node.lineno] = []
                    if full_nodes:
                        variable_defs[_use.node.lineno].append(_var.node)
                    else:
                        variable_defs[_use.node.lineno].append(_id)

        _visit_child_locals(node)

        return variable_defs, locals_defs

    # def visit_ClassDef(self, node):
    #     for stmt in node.body:
    #         if isinstance(stmt, gast.FunctionDef):
    #             self_def = self.chains.chains[stmt.args.args[0]]
    #             self.users.update(use.node for use in self_def.users())
    #     self.generic_visit(node)

    # def visit_Attribute(self, node):
    #     if node.value in self.users:
    #         self.attributes.add(node.attr)


# %%
# compute the def-use chains at module level
# self.duc = beniget.DefUseChains()
# self.duc.visit(_ast)
# self.variable_defs_nodes = self.duc.get_all_definitions_for_use(_ast, full_nodes=True)

# def get_all_variable_users(self, node):
#     variable_users = {}
#     for _var in self.locals[node]:
#         if isinstance(_var.node, ast.ClassDef):
#             _id = _var.node.name + ":" + str(_var.node.lineno)
#         elif isinstance(_var.node, ast.Name):
#             _id = _var.node.id + ":" + str(_var.node.lineno)
#         if not _id in variable_users:
#             variable_users[_id] = []
#         for _use in _var.users():
#             variable_users[_id].append(_use)

#     return variable_users

# NOTE: get definition from use
