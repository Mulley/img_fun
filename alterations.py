"""The alterations."""
import sys
import numpy as np


def weighted_average(pixel):
    """Greyscale of this pixel as a weighted average."""
    return .299*pixel[0]+.587*pixel[1]+.114*pixel[2]


def progress_bar(current_pos, total_size):
    """Progress bar."""
    formatted_string = format((current_pos/total_size)*100, '.2f').rstrip(
        '0').rstrip('.')
    sys.stdout.write('\r' + formatted_string)
    sys.stdout.flush()


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
