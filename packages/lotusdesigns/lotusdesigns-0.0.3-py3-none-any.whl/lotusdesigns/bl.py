"""
This module provides functionality for the shop's business logic.
"""

import os
from lotusdesigns.utils import read_json_file
from lotusdesigns.utils import expand_path


def parse_template_config(template_file_path):
    """
    Parse a JSON template configuration file, expand template paths to absolute
    paths, and return the updated configuration.

    Args:
        template_file_path (str): The path to the JSON template configuration
                                  file.

    Returns:
        list: A list of dictionaries representing the parsed and updated
              configuration.

    Raises:
        FileNotFoundError: If the specified template file does not exist.
    """
    config_data = read_json_file(template_file_path)

    template_file_dir = expand_path(os.path.dirname(template_file_path))

    for config in config_data:
        raw_template_path = config["template"]
        template_path = expand_path(raw_template_path, template_file_dir)
        config["template"] = template_path

    return config_data


def taxinomize_art_projects(root_dir):
    """
    Taxonomizes art projects based on their configuration files.

    Args:
        root_dir (str): The root directory containing art projects.

    Returns:
        dict: A dictionary representing the taxonomized art projects.
              Keys are image counts, and values are lists of project dictionaries.
    """
    rv = {}
    for foldername, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == "config.json":
                config_file_path = os.path.join(foldername, filename)
                data = read_json_file(config_file_path)
                name = data["project_name"]
                relative_photo_paths = data["photos"]

                image_count = len(relative_photo_paths)

                photos = [
                    os.path.join(foldername, photo) for photo in relative_photo_paths
                ]

                d = {}
                d["name"] = name
                d["photos"] = photos

                # Create an empty list for the key only if it doesn't exist
                if image_count not in rv:
                    rv[image_count] = []

                rv[image_count].append(d)
    return rv
