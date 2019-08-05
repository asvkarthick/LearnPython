#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

import os

cwd = os.getcwd()
filename = os.path.join(cwd, "output_file.txt")

with open(filename, 'r') as f:
    for line in f:
        print(line)
