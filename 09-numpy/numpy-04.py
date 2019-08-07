#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>
# Python program to create simple image

import numpy as np
from PIL import Image

rgb = np.zeros((1080, 1920, 3))
rgb[:, :, 0] = np.ones((1080, 1920)) * 255

image = Image.fromarray(rgb.astype(np.uint8))
image.save('red_image.jpg')
print('Red color image created')
