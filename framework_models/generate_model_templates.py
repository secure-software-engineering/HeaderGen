# %%
# import keras
import ast
import json
import os
import re
import shutil
from pathlib import Path

from framework_models.ml_function_classifier import MLFunctionClassifier

ml_function_classifier = MLFunctionClassifier.MLFunctionClassifier()

script_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

DATA_SCIECE_LIBRARY_DIR = f"{script_dir}/.env/lib/python3.10/site-packages"

LIBRARY_FUNTIONS = {}
out_path = f"{script_dir}/framework_models/_model"

try:
    shutil.rmtree(out_path)
except OSError:
    print("Removal of the directory %s failed" % out_path)

try:
    os.mkdir(out_path)
except OSError:
    print("Creation of the directory %s failed" % out_path)
else:
    print("Successfully created the directory %s " % out_path)


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
    "statsmodels": os.path.join(DATA_SCIECE_LIBRARY_DIR, "statsmodels"),
}

LIBRARY_FUNTIONS = {k: {} for k in ML_MODULES}


def get_relative_module_name(filepath, module_name, module_path):
    module_string = []
    for i in range(1, len(filepath.parts) + 1):
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
    print(f"Processing: {_library}")
    for _file in Path(_module_path).rglob("*.py"):
        module_name = get_relative_module_name(_file, _library, _module_path)
        source = open(_file).read()

        functions = [
            f"{_library}.{module_name}.{f.name}"
            for f in ast.parse(source).body
            if isinstance(f, ast.FunctionDef)
        ]

        functions_def = {
            f"{_library}.{module_name}.{f.name}": ast.get_docstring(f)
            for f in ast.parse(source).body
            if isinstance(f, ast.FunctionDef)
        }

        classes = [f for f in ast.parse(source).body if isinstance(f, ast.ClassDef)]

        for _class in classes:
            functions.extend(
                [
                    f"{_library}.{module_name}.{_class.name}.{f.name}"
                    for f in _class.body
                    if isinstance(f, ast.FunctionDef)
                ]
            )

            class_function_defs = {
                f"{_library}.{module_name}.{_class.name}.{f.name}": ast.get_docstring(f)
                for f in _class.body
                if isinstance(f, ast.FunctionDef)
            }

        for _class in classes:
            functions.extend(
                [f"{_library}.{module_name}.{_class.name}" for f in _class.body]
            )

            class_function_defs = {
                f"{_library}.{module_name}.{_class.name}": ast.get_docstring(f)
                for f in _class.body
                if isinstance(f, ast.ClassDef)
            }

            functions_def = functions_def | class_function_defs

        if module_name == "io.parsers.readers":
            print()

        LIBRARY_FUNTIONS[_library][module_name] = {
            k: ml_function_classifier.predict_function(k, str(d))
            for k, d in functions_def.items()
        }
        json_path = f'{out_path}/{_library}/{module_name.replace(".","/")}.json'
        try:
            os.makedirs(re.sub("(\/[^\/]+)\/?$", "", json_path))
        except FileExistsError:
            pass
            # print("Directory already exists")

        with open(f"{json_path}", "w") as outfile:
            json.dump(LIBRARY_FUNTIONS[_library][module_name], outfile, indent=4)

print()
