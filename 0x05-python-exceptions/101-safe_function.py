#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """A function that executes safely."""
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
