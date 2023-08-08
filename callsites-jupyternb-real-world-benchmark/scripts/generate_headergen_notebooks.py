# %%
import errno
import logging
import os
import shutil
import time
import traceback
from pathlib import Path

import simplejson as sjson

from headergen import headergen

# Careful, the out_path folder will be removed
in_ipynb_path = r"/app/HeaderGen/callsites-jupyternb-real-world-benchmark/notebooks"
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

        analysis_meta = headergen.start_headergen(str(_file), out_path, debug_mode=True)

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

        with open("{}/{}-metadata.json".format(comp_path, _file.stem), "w") as outfile:
            sjson.dump(
                analysis_meta,
                outfile,
                indent=4,
                iterable_as_array=True,
            )

        logging.debug("DONE")

    except Exception as e:
        logging.error("Root level Exception: {:02}-{}".format(notebook_id, _file.stem))
        logging.error(_file)
        logging.error(e)
        logging.error(traceback.format_exc())

        print(e)
        failures = failures + 1
    logging.debug("=======================================================\n")
    count = count + 1

print(f"Analysis took: {time.time() - start}")
print(f"Failed: {failures}/{count}")
