# %%
from pathlib import Path
import logging
import os, errno
import shutil

from pycg_extended import pycg
from pycg_extended import formats as pycg_formats

import simplejson as sjson
import utils
from importlib import reload
from headergen import headergen
import time
import requests

headergen_url = "http://127.0.0.1:8080"
# Careful, the out_path folder will be removed
in_ipynb_path = r"/tmp/callsites-jupyternb-real-world-benchmark/notebooks"
out_path = r"/results/annotated_notebooks"

# Remove results dir and recreate
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

SAVE_HEADERGEN_OUTPUT = True

# Logging
logging.basicConfig(
    filename="{}/logs.log".format(out_path),
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
    level=3,
)
logging.info("Data-prep started")

response = requests.get(f"{headergen_url}")
print(response)

# %%
# Find all notebooks in location
notebook_id = 1
count = 0
failures = 0
start = time.time()
for _file in sorted(Path(in_ipynb_path).rglob("*.ipynb")):
    try:
        notebook_id += 1

        logging.debug("###################################################\n")
        logging.debug(_file.name)
        print(_file.name)
        comp_path = os.path.join(out_path)

        analysis_meta = requests.get(
            f"{headergen_url}/get_analysis_notebook?file_path={str(_file)}"
        ).json()

        block_mapping = {}
        ignore_tags = ["Unknown"]
        for _cell, _cell_block in analysis_meta["block_mapping"].items():
            block_mapping[_cell] = [
                x for x in set(_cell_block["dl_pipeline_tag"]) if x not in ignore_tags
            ]

        func_mapping = {}
        for _cs in analysis_meta["analysis_info"]["context_library_calls"].values():
            for _call in _cs:
                func_mapping[_call["func_call"]] = _call["dl_pipeline_tag"]

        with open("{}/{}-headers.json".format(comp_path, _file.stem), "w") as outfile:
            sjson.dump(
                dict(sorted(block_mapping.items())),
                outfile,
                indent=4,
                iterable_as_array=True,
            )

        with open("{}/{}-mapping.json".format(comp_path, _file.stem), "w") as outfile:
            sjson.dump(
                dict(sorted(func_mapping.items())),
                outfile,
                indent=4,
                iterable_as_array=True,
            )

        with open("{}/{}-cs.json".format(comp_path, _file.stem), "w") as outfile:
            sjson.dump(
                dict(
                    sorted(
                        analysis_meta["cell_callsites"].items(), key=lambda e: int(e[0])
                    )
                ),
                outfile,
                indent=4,
                iterable_as_array=True,
            )

        logging.debug("DONE")

    except Exception as e:
        logging.error("Root level Exception: {:02}-{}".format(notebook_id, _file.stem))
        logging.error(_file)
        logging.error(e)
        print(e)
        failures = failures + 1
    logging.debug("=======================================================\n")
    count = count + 1

print(f"Analysis took: {time.time() - start}")
print(f"Failed: {failures}/{count}")
# -----------------------------
# After Annotation
# Create an extractor to retreive data back
# Export as a usable dataset
