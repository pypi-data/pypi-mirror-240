import os
import json
import importlib.metadata


def get_version():
    version = importlib.metadata.version('lotusDesigns')
    return version

def expand_path(path):
    """
    Expand a path to its full absolute path, handling relative, absolute, and ~-prefixed paths.
    """
    if path.startswith("~"):
        # Expand ~ to the user's home directory
        path = os.path.expanduser(path)
    elif not path.startswith("/") and not os.path.isabs(path):
        # Handle relative paths by making them absolute relative to the current working directory
        path = os.path.abspath(path)

    return path


def readJsonFile(json_file_path):
    """Open the JSON file for reading"""
    data = {}
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
    return data


def pretty_print_json(json_obj):
    pretty_json = json.dumps(json_obj, indent=4)
    print(pretty_json)
