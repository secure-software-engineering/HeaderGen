from _typeshed import Incomplete

MY_PACKAGE: Incomplete

def local_script_dir(script_sdir): ...
def local_module_dir(module_name): ...

class ScriptRunner:
    local_script_dir: Incomplete
    local_module_dir: Incomplete
    debug_print: Incomplete
    output_processor: Incomplete
    def __init__(
        self,
        script_sdir: str = "scripts",
        module_sdir=...,
        debug_print_var: Incomplete | None = None,
        output_processor=...,
    ) -> None: ...
    def run_command(self, cmd, check_code: bool = True): ...
