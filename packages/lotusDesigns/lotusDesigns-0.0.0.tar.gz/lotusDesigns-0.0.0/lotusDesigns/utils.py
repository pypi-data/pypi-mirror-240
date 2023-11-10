import os
import json
import re
import subprocess
import importlib.metadata
from importlib.metadata import PackageNotFoundError
from subprocess import CalledProcessError

def get_git_version():
    version = None
    try:
        result = subprocess.run(['git', 'describe', '--tags', '--abbrev=0'], capture_output=True, text=True, check=True)
        version = result.stdout.strip()
    except CalledProcessError as e:
        print(f"Error getting version: {e}")
        raise Exception("Failed to get version from git")

    if version is not None:
        version = version.lstrip('v')

    if varsion is not None and not is_canonical(version):
        raise Exception(f"Invalid version from Git: {version}")

    return version


def get_version():
    def is_canonical(version):
        return re.match(r'^([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))*((a|b|rc)(0|[1-9][0-9]*))?(\.post(0|[1-9][0-9]*))?(\.dev(0|[1-9][0-9]*))?$', version) is not None

    version = None
    try:
        version = importlib.metadata.version('lotusDesigns')
    except PackageNotFoundError:
        # If package metadata not found, try to get version from Git
        try:
            result = subprocess.run(['git', 'describe', '--tags', '--abbrev=0'], capture_output=True, text=True, check=True)
            version = result.stdout.strip()

            version = version.lstrip('v')

            if not is_canonical(version):
                raise Exception(f"Invalid version from Git: {version}")

        except CalledProcessError as e:
            print(f"Error getting version: {e}")
            version = "0.0.0"

    except Exception as e:
        print(e)
        import sys
        sys.exit(1)

    if not is_canonical(version):
        raise Exception(f"Invalid version: {version}")

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
