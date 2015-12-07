import os
import numpy as np
from scipy.misc import imread, imsave

path = 'resources/Roger.jpg'
image_data = imread(path)
print(os.path.splitext(path)[0])
print(os.path.splitext(os.path.basename(path))[0])
"""
print(type(image_data))
print(image_data.shape)
print(image_data.size)
print(image_data.data)
print(image_data.dtype)
print(image_data[0][0])
"""
