import sys
import json


def log_msg(*msg, debug=None, dict=None):  # pragma: no cover
    if debug:
        if msg:
            print(*msg, sep='\n')
        if dict is not None:
            if sys.implementation.name == "micropython":
                print(json.dumps(dict))
            else:
                print(json.dumps(dict, indent=4))
