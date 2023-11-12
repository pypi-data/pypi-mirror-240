"""
The main application.
"""

import os
import sys
from lotusdesigns.photo import Photo
from lotusdesigns.args import parse_args
from lotusdesigns.config import ensure_config
from lotusdesigns.config import get_config
from lotusdesigns.utils import get_version
from lotusdesigns.utils import expand_path
from lotusdesigns.utils import pretty_print_json
from lotusdesigns.bl import taxinomize_art_projects
from lotusdesigns.bl import parse_template_config

# pylint: disable=too-many-locals
def do_work(
    is_verbose, template_image, out_directory_path, set_of_art, template_config
):
    """
    Generates an art project based on the provided parameters.

    Args:
        is_verbose (bool): Whether to enable verbose mode.
        template_image: An object representing the template image.
        out_directory_path (str): The path to the output directory.
        set_of_art (dict): A dictionary containing information about the art project.
        template_config (dict): A dictionary containing template configuration.

    Raises:
        ValueError: If the A and D points of an image are invalid.
    """
    name = set_of_art["name"]
    photos = set_of_art["photos"]

    placeholders = template_config["placeholders"]
    template_name = template_config["name"]

    if is_verbose:
        print(f"Generating project '{name}' with template '{template_name}'.")

    for photo, placeholder in zip(photos, placeholders):
        x = int(placeholder["x"])
        y = int(placeholder["y"])
        dx = int(placeholder["Dx"])
        dy = int(placeholder["Dy"])

        width = dx - x
        height = dy - y
        if width <= 0 or height <= 0:
            raise ValueError("Width and/or heigth is zero or negative")

        overlay_image_path = photo
        overlay_image = Photo(overlay_image_path)
        overlay_image.scale(width, height)
        template_image.add_overlay(overlay_image, x, y)

    directory_path = os.path.join(out_directory_path, name)
    out_image_path = os.path.join(directory_path, f"{template_name}.png")
    os.makedirs(directory_path, exist_ok=True)
    template_image.save(out_image_path)
    print(f"Saved '{out_image_path}'")


def app():
    """
    Main application logic.

    Raises:
        FileNotFoundError: Could not find the template file.
    """
    try:
        ensure_config()
        args = parse_args()

        if args.version:
            version = get_version()
            print(version)
            sys.exit(0)

        # Template path
        template_file_path = expand_path(get_config("template_file_path"))
        if args.template is not None:
            arg_template_file_path = expand_path(args.template)
            if not os.path.isfile(arg_template_file_path):
                raise FileNotFoundError(
                    f"No template found with file name '{arg_template_file_path}'."
                )

            template_file_path = arg_template_file_path

        # Parse template
        config_data = parse_template_config(template_file_path)
        if args.verbose:
            print("Template information")
            pretty_print_json(config_data)

        # Out dir path
        out_dir_path = expand_path(get_config("out_directory_path"))
        if args.outDir is not None:
            out_dir_path = expand_path(args.outDir)

        # Parse art
        art_directory_path = expand_path(args.art_path)
        art_data = taxinomize_art_projects(art_directory_path)

        if args.verbose:
            print("Art information")
            pretty_print_json(art_data)

        # ----------------
        for config in config_data:
            template_image_path = config["template"]
            template_image = Photo(template_image_path)
            placeholders = config["placeholders"]
            number_of_placeholders = len(placeholders)

            for set_of_art in art_data.get(number_of_placeholders, []):
                do_work(args.verbose, template_image, out_dir_path, set_of_art, config)

    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")
        sys.exit(1)


if __name__ == "__main__":
    app()
