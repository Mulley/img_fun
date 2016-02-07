"""Stop."""
import os
import argparse
from alterations import (convert_to_absolute_grey,
                         convert_to_weighted_grey,
                         shift_color_value_left,
                         shift_color_value_right,
                         to_nearest_color)


def get_args():
    """Get commandline args."""
    parser = argparse.ArgumentParser(description='Process an image')
    parser.add_argument('alteration', choices=[
        'grey', 'grey_weighted', 'shift_left', 'shift_right'])

    return parser.parse_args()


def perform_alteration(image, choice):
    """Perform specified alteration."""
    alt_image = None
    if choice.alteration == 'grey':
        alt_image = convert_to_absolute_grey(image)
    elif choice.alteration == 'grey_weighted':
        alt_image = convert_to_weighted_grey(image)
    elif choice.alteration == 'shift_left':
        alt_image = shift_color_value_left(image)
    elif choice.alteration == 'shift_right':
        alt_image = shift_color_value_right(image)
    elif choice.alteration == 'nearest_color':
        alt_image = to_nearest_color(image)
    else:
        print("argparse means you shouldn't get here")
    return alt_image


def new_file_name(path, choice):
    """
    Return a string for the new file name.

    path is the original path, choice is the arument from argparser
    Original path is preserved.
    """
    name = os.path.splitext(path)[0]
    extension = os.path.splitext(os.path.basename(path))[1]

    return name + choice.alteration + extension
