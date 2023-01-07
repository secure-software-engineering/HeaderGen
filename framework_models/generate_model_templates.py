# %%
# import keras
import os
from pathlib import Path
from inspect import getmembers, isfunction
import ast
import json
import re
import shutil

DATA_SCIECE_LIBRARY_DIR = "/usr/local/lib/python3.9/site-packages"
LIBRARY_FUNTIONS = {}
out_path = "/tmp/framework_models/_model"

try:
    shutil.rmtree(out_path)
except OSError:
    print ("Removal of the directory %s failed" % out_path)

try:
    os.mkdir(out_path)
except OSError:
    print ("Creation of the directory %s failed" % out_path)
else:
    print ("Successfully created the directory %s " % out_path)


ML_MODULES = {
    "pandas": os.path.join(DATA_SCIECE_LIBRARY_DIR, "pandas"),
    "numpy": os.path.join(DATA_SCIECE_LIBRARY_DIR, "numpy"),
    "matplotlib": os.path.join(DATA_SCIECE_LIBRARY_DIR, "matplotlib"),
    "keras": os.path.join(DATA_SCIECE_LIBRARY_DIR, "keras"),
    "sklearn": os.path.join(DATA_SCIECE_LIBRARY_DIR, "sklearn"),
    "tensorflow": os.path.join(DATA_SCIECE_LIBRARY_DIR, "tensorflow"),
    "lightgbm": os.path.join(DATA_SCIECE_LIBRARY_DIR, "lightgbm"),
    "plotly": os.path.join(DATA_SCIECE_LIBRARY_DIR, "plotly"),
    "scipy": os.path.join(DATA_SCIECE_LIBRARY_DIR, "scipy"),
    "xgboost": os.path.join(DATA_SCIECE_LIBRARY_DIR, "xgboost"),
    "statsmodels": os.path.join(DATA_SCIECE_LIBRARY_DIR, "statsmodels")
}

LIBRARY_FUNTIONS = { 
    k: {} for k in ML_MODULES
}

def get_relative_module_name(filepath, module_name, module_path):
    module_string = []
    for i in range(1,len(filepath.parts)+1):
        if filepath.parts[-i].startswith("__init__"):
            if str(filepath.parent) == module_path:
                module_string.append(module_name)
                break
        elif filepath.parts[-i] == Path(module_path).stem:
            # module_string.append(module_name)
            break
        else:
            if filepath.parts[-i].endswith(".py"):
                module_string.append(filepath.stem)
            else:
                module_string.append(filepath.parts[-i])

    return ".".join(reversed(module_string))

for _library, _module_path in ML_MODULES.items():
    for _file in Path(_module_path).rglob('*.py'):
        module_name = get_relative_module_name(_file, _library, _module_path)
        source = open(_file).read()

        functions = [f"{_library}.{module_name}.{f.name}" for f in ast.parse(source).body
             if isinstance(f, ast.FunctionDef)]

        classes = [f for f in ast.parse(source).body
             if isinstance(f, ast.ClassDef)]

        for _class in classes:
            functions.extend([f"{_library}.{module_name}.{_class.name}.{f.name}" for f in _class.body
             if isinstance(f, ast.FunctionDef)])

        for _class in classes:
            functions.extend([f"{_library}.{module_name}.{_class.name}" for f in _class.body])

        if module_name == "core.generic":
            print()

        LIBRARY_FUNTIONS[_library][module_name] =  {k: [] for k in functions }
        json_path = f'{out_path}/{_library}/{module_name.replace(".","/")}.json'
        try:
            os.makedirs(re.sub("(\/[^\/]+)\/?$", "", json_path))
        except FileExistsError:
            pass
            # print("Directory already exists")  

        with open(f'{json_path}', 'w') as outfile:
                    json.dump(LIBRARY_FUNTIONS[_library][module_name], outfile, indent=4)

print()
