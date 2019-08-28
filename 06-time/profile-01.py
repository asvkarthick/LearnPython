#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>
# Python program to create simple image

import numpy as np
from PIL import Image
import time

# Start timer
t_start = time.time()

rgb = np.zeros((1080, 1920, 3))
rgb[:, :, 0] = np.ones((1080, 1920)) * 255

image = Image.fromarray(rgb.astype(np.uint8))
image.save('red_image.jpg')
print('Red color image created')

# Stop the timer
t_end = time.time()
t_diff = t_end - t_start
print('Time taken = ', t_diff)
