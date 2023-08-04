import os
import sys
from pathlib import Path

import simplejson as sjson

from framework_models import get_high_level_phase
from headergen import headergen

script_dir = os.path.abspath(os.path.dirname(__file__))


def main():
    file_path = sys.argv[1]

    # Check if the path exists
    if not os.path.exists(file_path):
        print("Error: The specified path does not exist.")
        return

    analysis_meta = headergen.start_headergen(file_path, "/tmp", debug_mode=True)

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

    with open(
        "{}/{}_metadata.json".format(script_dir, Path(file_path).stem), "w"
    ) as outfile:
        sjson.dump(
            analysis_output,
            outfile,
            indent=4,
            iterable_as_array=True,
        )

    print("OK", end="")
    return "OK"


if __name__ == "__main__":
    main()
