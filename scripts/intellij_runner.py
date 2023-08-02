import os
import sys

import simplejson as sjson

from headergen import headergen

script_dir = os.path.abspath(os.path.dirname(__file__))


def main():
    file_path = sys.argv[1]

    # Check if the path exists
    if not os.path.exists(file_path):
        print("Error: The specified path does not exist.")
        return

    analysis_meta = headergen.get_analysis_output(file_path, "/tmp")

    with open("{}/metadata.json".format(script_dir), "w") as outfile:
        sjson.dump(
            analysis_meta,
            outfile,
            indent=4,
            iterable_as_array=True,
        )

    return "OK"


if __name__ == "__main__":
    main()
