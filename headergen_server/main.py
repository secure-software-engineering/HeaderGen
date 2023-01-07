from fastapi import FastAPI
from fastapi.responses import FileResponse
from headergen import headergen
from pathlib import Path
import uvicorn

import logging
import os, errno
import shutil

import time

out_path = r"/tmp"

app = FastAPI()
RETRY_SLEEP = 0.25
DEBUG_MODE = True


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
    return {"Hello": "HeaderGen Server"}


@app.get("/get_analysis_notebook")
def get_analysis(file_path: str = ""):
    is_safe = is_path_safe(file_path)
    if not is_safe[0]:
        return is_safe[1]
    else:
        analysis_meta = headergen.start_headergen(
            str(file_path), out_path, debug_mode=DEBUG_MODE
        )

    return analysis_meta


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
    uvicorn.run(app, host="0.0.0.0", port=8080)

# uvicorn --reload --host 0.0.0.0 --port 8080 main:app
