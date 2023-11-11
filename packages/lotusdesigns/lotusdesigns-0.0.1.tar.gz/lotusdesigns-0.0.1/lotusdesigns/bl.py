"""
This module provides functionality for the shop's business logic.
"""

import os
from lotusdesigns.utils import read_json_file


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
