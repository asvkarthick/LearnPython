#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

import os

cwd = os.getcwd()
print(cwd)

filename = os.path.join(cwd, "output_file.txt")
print(filename)

fd = open(filename, "w")
fd.write("Karthick\n")
fd.write("Karthick Kumaran\n")
fd.close()
