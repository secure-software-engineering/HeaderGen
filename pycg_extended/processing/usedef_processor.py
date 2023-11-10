import gast

from beniget import beniget

# NOTE: Flow Sensitive


# Class to fetch all uses of self vars in a class
class Attributes(gast.NodeVisitor):
    def __init__(self, module_node, class_name):
        # compute the def-use of the module
        self.chains = beniget.DefUseChains()
        self.chains.visit(module_node)
        self.users = set()  # all users of `self`
        self.attributes = []  # attributes of current class
        self.class_name = class_name
        self.function_scopes = {}

    def visit_ClassDef(self, node):
        # walk methods and fill users of `self`
        for stmt in node.body:
            if isinstance(stmt, gast.FunctionDef):
                if stmt.args.args:
                    self_def = self.chains.chains[stmt.args.args[0]]
                    self.users.update(use.node for use in self_def.users())
                    self.function_scopes = self.function_scopes | {
                        str(use.node): stmt.name for use in self_def.users()
                    }

        self.generic_visit(node)

    def visit_Attribute(self, node):
        # any attribute of `self` is registered
        if node.value in self.users:
            if isinstance(node.ctx, gast.Store):
                self.attributes.append(
                    {
                        "name": f"{self.class_name}.{node.attr}",
                        "lineno": node.lineno,
                        "function": self.function_scopes.get(str(node.value), ""),
                    }
                )


class UseDefProcessor(gast.NodeVisitor):
    use_def_cache = {}

    def __init__(self, module_path):
        self.module_path = module_path
        self.module_node = gast.parse(open(module_path).read())

        self.duc = beniget.DefUseChains()
        self.duc.visit(self.module_node)

        self.udc = beniget.UseDefChains(self.duc)
        self.locals_defs_modules = {}

        if module_path not in UseDefProcessor.use_def_cache:
            self.analyze()
        else:
            self.line_uses = UseDefProcessor.use_def_cache[module_path]["line_uses"]
            self.locals_defs = UseDefProcessor.use_def_cache[module_path]["locals_defs"]
            self.class_vars = UseDefProcessor.use_def_cache[module_path]["class_vars"]
            self.locals_defs_modules[module_path] = UseDefProcessor.use_def_cache[
                module_path
            ]["locals_defs"]

    def analyze(self):
        self.generic_visit(self.module_node)
        (
            self.line_uses,
            self.locals_defs,
            self.class_vars,
        ) = self.get_all_definitions_for_use()
        self.locals_defs_modules[self.module_path] = self.locals_defs
        UseDefProcessor.use_def_cache[self.module_path] = {
            "line_uses": self.line_uses,
            "locals_defs": self.locals_defs,
            "class_vars": self.class_vars,
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
        class_vars = []

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
                if isinstance(_var.node, gast.ClassDef):
                    _id = _var.node.name + ":" + str(_var.node.lineno)
                    self.attr = Attributes(self.module_node, _id)
                    self.attr.visit(_var.node)
                    class_vars.extend(self.attr.attributes)
                    _visit_child_locals(_var.node)
                elif isinstance(_var.node, gast.FunctionDef):
                    _id = _var.node.name + ":" + str(_var.node.lineno)
                    _visit_child_locals(_var.node)
                elif isinstance(_var.node, gast.Name):
                    if not hasattr(_var.node, "lineno"):
                        continue
                    _id = _var.node.id + ":" + str(_var.node.lineno)
                    if isinstance(_var.node.ctx, gast.Param):
                        _node_type = "param"
                    else:
                        _node_type = "local_variable"

                    _def_info = {
                        "name": _id,
                        "id": _var.node.id,
                        "lineno": _var.node.lineno,
                        "node_type": _node_type,
                    }
                    locals_defs.append(_def_info)
                elif isinstance(_var.node, gast.alias):
                    if _var.node.asname:
                        _id = _var.node.asname
                    else:
                        _id = _var.node.name
                # elif isinstance(_var.node, gast.Attribute):
                #     _id = _var.node.name + ":" + str(_var.node.lineno)
                #     _visit_child_locals(_var.node)

                for _use in _var.users():
                    if not _use.node.lineno in variable_defs:
                        variable_defs[_use.node.lineno] = []
                    if full_nodes:
                        variable_defs[_use.node.lineno].append(_var.node)
                    else:
                        variable_defs[_use.node.lineno].append(_id)

                # TODO: Revisit collection of uses

        _visit_child_locals(node)

        return variable_defs, locals_defs, class_vars

    # def visit_ClassDef(self, node):
    #     for stmt in node.body:
    #         if isinstance(stmt, gast.FunctionDef):
    #             self_def = self.chains.chains[stmt.args.args[0]]
    #             self.users.update(use.node for use in self_def.users())
    #     self.generic_visit(node)

    # def visit_FunctionDef(self, node):
    #     # initialize the set of node using a local variable
    #     for def_ in self.duc.locals[node]:
    #         l = [use.node for use in def_.users()]
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
