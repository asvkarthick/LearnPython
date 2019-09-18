#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

import os

infile = open('input.jpg', 'rb')
outfile = open('output.jpg', 'wb')

while True:
    buf = infile.read(100);
    if buf:
        outfile.write(buf)
        print('.', end = '', flush = True)
    else:
        break
outfile.close()
print('Image copying done')
