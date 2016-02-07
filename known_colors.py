"""Colors for the distance alteration."""
import numpy as np
# Primary Colors
RED = {'r': 255, 'g': 0, 'b': 0}
BLUE = {'r': 0, 'g': 0, 'b': 255}
YELLOW = {'r': 255, 'g': 255, 'b': 0}
# Secondary Colors
ORANGE = {'r': 255, 'g': 165, 'b': 0}
GREEN = {'r': 0, 'g': 255, 'b': 0}
PURPLE = {'r': 155, 'g': 48, 'b': 255}
# Other Colors
BLACK = {'r': 0, 'g': 0, 'b': 0}
GRAY = {'r': 40, 'g': 40, 'b': 40}
LIGHT_GRAY = {'r': 190, 'g': 190, 'b': 190}
WHITE = {'r': 255, 'g': 255, 'b': 255}
# Carcassone Colors
RIVER = {'r': 115, 'g': 115, 'b': 115}
GOLDENROD = {'r': 180, 'g': 100, 'b': 60}
FIELD = {'r': 115, 'g': 130, 'b': 40}


COMPARISON_LIST = [FIELD, RIVER, GOLDENROD, BLACK]


def get_numpy_list(colors=COMPARISON_LIST):
    """Return COMPARISON_LIST as a list of numpy arrays."""
    np_list = []
    for color in colors:
        np_list.append(np.array((color['r'], color['g'], color['b'])))

    return np_list
