"""
Generic utilities.
"""

import os
import json


def get_version():
    """
    Get the version of the package.

    Returns:
        str: The version string.
    """
    version = "unknown"

    try:
        # pylint: disable=import-error disable=import-outside-toplevel
        from lotusdesigns._version import __version__

        version = __version__
    except ImportError:
        pass

    return version


def expand_path(path, base_path=None):
    """
    Expand a path to its full absolute path, handling relative, absolute, and ~-prefixed paths.

    Args:
        path (str): The path to be expanded.
        base_path (str, optional): The base path to be used for relative paths. Defaults to None.

    Returns:
        str: The expanded absolute path.

    Raises:
        ValueError: If `path` is not a valid string.
    """
    if path.startswith("~"):
        # Expand ~ to the user's home directory
        path = os.path.expanduser(path)
    elif not path.startswith("/") and not os.path.isabs(path):
        if base_path is None:
            # Handle relative paths by making them
            # absolute relative to the current working directory
            path = os.path.abspath(path)
        else:
            # Handle relative paths by making them
            # absolute relative to the provided directory directory
            path = os.path.abspath(os.path.join(base_path, path))

    return path


def read_json_file(json_file_path):
    """
    Open the JSON file for reading.

    Args:
        json_file_path (str): The path to the JSON file.

    Returns:
        dict: The parsed JSON data.
    """
    data = {}
    with open(json_file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def pretty_print_json(json_obj):
    """
    Pretty print a JSON object.

    Args:
        json_obj (dict): The JSON object to be pretty printed.
    """
    pretty_json = json.dumps(json_obj, indent=4)
    print(pretty_json)
