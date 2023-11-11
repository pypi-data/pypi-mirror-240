"""
Module for dealing with configuration operations.
"""

import os
import shutil
import yaml
from xdg_base_dirs import xdg_config_home


def get_package_name():
    """
    Gets the package name.

    Returns:
        str: The package name.
    """
    return "lotusdesigns"


def get_skeleton_root_dir():
    """
    Gets the root directory of the skeleton files.

    Returns:
        str: The root directory of the skeleton files.
    """
    script_directory = os.path.dirname(os.path.abspath(__file__))
    template_root_dir = os.path.join(script_directory, "skeleton")
    return template_root_dir


def ensure_config():
    """
    Make sure that the configs are present.
    Create default ones if not present from the skeleton files.
    """
    package_name = get_package_name()
    config_file_name = "config.yml"
    template_config_file_name = "template.json"
    image_file_name = "template.jpg"

    # We want to ensure that the configuration directory is present.
    config_file_dir = os.path.join(xdg_config_home(), package_name)
    if not os.path.exists(config_file_dir):
        os.makedirs(config_file_dir, exist_ok=True)

    # We want to ensure that the configuration file is present.
    config_file_path = os.path.join(config_file_dir, config_file_name)
    if not os.path.exists(config_file_path):
        # Read the contents of the template config file
        config_file_path_skeleton = os.path.join(
            get_skeleton_root_dir(), config_file_name
        )
        contents = ""
        with open(config_file_path_skeleton, "r", encoding="utf-8") as file:
            contents = file.read()

        # Write the contents to the config file
        with open(config_file_path, "w", encoding="utf-8") as file:
            file.write(contents)

    # We want to ensure that the template configuration file is present.
    template_config_file_path = os.path.join(config_file_dir, template_config_file_name)
    if not os.path.exists(template_config_file_path):
        # Read the contents of the template config file
        template_config_file_path_skeleton = os.path.join(
            get_skeleton_root_dir(), template_config_file_name
        )
        contents = ""
        with open(template_config_file_path_skeleton, "r", encoding="utf-8") as file:
            contents = file.read()

        # Write the contents to the config file
        with open(template_config_file_path, "w", encoding="utf-8") as file:
            file.write(contents)

    # This photo is used by the default template configuration
    image_file_path = os.path.join(config_file_dir, image_file_name)
    if not shutil.os.path.exists(image_file_path):
        # Copy the file if the destination file does not exist
        image_file_path_skeleton = os.path.join(
            get_skeleton_root_dir(), image_file_name
        )
        shutil.copy2(image_file_path_skeleton, image_file_path)


def get_config(key):
    """
    Gets the configuration value for the specified key.

    Args:
        key (str): The key for which to get the configuration value.

    Returns:
        Any: The configuration value.

    Raises:
        ValueError: If the value for the specified key is None.
    """
    package_name = get_package_name()
    config_file_name = "config.yml"
    config_file_dir = os.path.join(xdg_config_home(), package_name)
    config_file_path = os.path.join(config_file_dir, config_file_name)

    with open(config_file_path, "r", encoding="utf-8") as file:
        config_data = yaml.safe_load(file)

    value = None
    if key in config_data:
        value = config_data[key]

    if value is None:
        raise ValueError(f"The value of '{key}' is '{value}'")

    return value
