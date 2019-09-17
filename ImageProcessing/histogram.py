#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

def histogram(h):
    hist = {}
    for x in h:
        hist[x] = hist.get(x, 0) + 1
    return hist

h = [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 0, 0, 0]
print(histogram(h))
