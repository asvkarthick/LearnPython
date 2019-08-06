#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>
# Program to print contents of directory

import os

cwd = os.getcwd()
dirs = os.listdir(cwd)
print(dirs)
