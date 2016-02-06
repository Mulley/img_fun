"""The alterations."""
import sys
import numpy as np
from known_colors import get_numpy_list, COMPARISON_LIST


def weighted_average(pixel):
    """Greyscale of this pixel as a weighted average."""
    return .299*pixel[0]+.587*pixel[1]+.114*pixel[2]


def progress_bar(current_pos, total_size):
    """Progress bar."""
    formatted_string = format((current_pos/total_size)*100, '.2f').rstrip(
        '0').rstrip('.')
    sys.stdout.write('\r' + formatted_string)
    sys.stdout.flush()


def get_nearest_color(pixel):
    """Return the RGB of the nearest color to the given pixel."""
    distances = []
    np_pixel = np.array((pixel[0], pixel[1], pixel[2]))
    for color in get_numpy_list():
        distances.append(np.linalg.norm(color-np_pixel))

    for i, distance in enumerate(distances):
        if distance == min(distances):
            return COMPARISON_LIST[i]


def convert_to_weighted_grey(image):
    """Convert pixel to greyscale with weighted average value."""
    grey = np.zeros((image.shape[0], image.shape[1]))
    for row in range(len(image)):
        for col in range(len(image[row])):
            grey[row][col] = weighted_average(image[row][col])
            progress_bar(row, len(image))

    return grey


def convert_to_absolute_grey(image):
    """Convert pixel to greyscale with average value."""
    grey = np.zeros((image.shape[0], image.shape[1]))
    for row in range(len(image)):
        for col in range(len(image[row])):
            grey[row][col] = np.average(image[row][col])
            progress_bar(row, len(image))

    return grey


def shift_color_value_right(image):
    """
    Shift the values of the colors of the pixels to the right.

    Red gets Blue. Green gets Red. Blue gets Green.
    """
    for row in range(len(image)):
        for col in range(len(image[row])):
            image[row][col] = [
                image[row][col][2], image[row][col][0], image[row][col][1]]
            progress_bar(row, len(image))

    return image


def shift_color_value_left(image):
    """
    Shift the values of the colors of the pixels to the right.

    Red gets Green. Green gets Blue. Blue gets Red.
    """
    for row in range(len(image)):
        for col in range(len(image[row])):
            image[row][col] = [
                image[row][col][1], image[row][col][2], image[row][col][0]]
            progress_bar(row, len(image))

    return image


def to_nearest_color(image):
    """Change pixel color to nearest comparison value."""
    for row in range(len(image)):
        for col in range(len(image[row])):
            nearest_color = get_nearest_color(image[row][col])
            image[row][col] = [
                nearest_color['r'], nearest_color['g'], nearest_color['b']]
            progress_bar(row, len(image))

    return image
