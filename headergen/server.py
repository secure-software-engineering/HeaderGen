import errno
import logging
import os
import shutil
import time
from pathlib import Path
from typing import Any, Dict

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

from framework_models import PHASES, get_high_level_phase, lookup_pipeline_tag
from headergen import headergen

out_path = r"/tmp"

app = FastAPI()
RETRY_SLEEP = 0.25
DEBUG_MODE = False


def is_path_safe(file_path):
    if not file_path:
        return False, "'file_path' is empty"
    if not Path(file_path).is_absolute():
        return False, "'file_path' is relative. Use absolute."
    if not Path(file_path).suffix in [".ipynb", ".py"]:
        return False, "'file_path' is not a notebook."
    # TODO:
    # Add safe dir to avoid traversal attacks

    return True, "ok"


@app.get("/")
def read_root():
    return "HeaderGen"


@app.get("/get_types")
def get_types(file_path: str = ""):
    is_safe = is_path_safe(file_path)
    if not is_safe[0]:
        return is_safe[1]
    else:
        analysis_meta = headergen.get_analysis_output(str(file_path), out_path)

    return analysis_meta["types_formatted"]


@app.get("/get_analysis_notebook")
def get_analysis(file_path: str = ""):
    is_safe = is_path_safe(file_path)
    if not is_safe[0]:
        return is_safe[1]
    else:
        analysis_meta = headergen.start_headergen(
            str(file_path), out_path, debug_mode=DEBUG_MODE
        )

    analysis_output = {
        "cell_callsites": analysis_meta["cell_callsites"],
        "block_mapping": {},
    }

    if "block_mapping" in analysis_meta:
        for _cell, _cell_results in analysis_meta["block_mapping"].items():
            analysis_output["block_mapping"][_cell] = list(
                set(
                    [
                        get_high_level_phase(x)
                        for x in _cell_results["dl_pipeline_tag_counter"]
                        if x
                        not in ["Unknown", "Function Definition", "Builtin Function"]
                    ]
                )
            )

    return analysis_output


@app.post("/get_ml_labels")
def get_ml_labels(payload: Dict[Any, Any]):
    result = {}
    for func, doc_string in payload.items():
        if "docstring" in doc_string:
            result[func] = [
                get_high_level_phase(x)
                for x in lookup_pipeline_tag(func, doc_string["docstring"])
            ]
        else:
            result[func] = [PHASES["UNKNOWN"]]

    return result


@app.get("/generate_annotated_notebook")
def generate_annotated_notebook(file_path: str = ""):
    is_safe = is_path_safe(file_path)
    if not is_safe[0]:
        return is_safe[1]
    else:
        analysis_meta = headergen.start_headergen(
            str(file_path), out_path, debug_mode=DEBUG_MODE
        )
        return FileResponse(
            analysis_meta["out_file"],
            media_type="application/octet-stream",
            filename=Path(analysis_meta["out_file"]).name,
        )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=54068)

# uvicorn --reload --host 0.0.0.0 --port 8080 main:app
