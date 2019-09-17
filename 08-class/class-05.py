#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

class Circle(object):
    def __init__(self, radius):
        self._radius = radius;

    def print_radius(self):
        print(self._radius)

    def radius(self, r = None):
        if r: self._radius = r
        return self._radius

    def __str__(self):
        return 'Radius = {}'.format(self._radius)

circle = Circle(5)
print(circle)
circle.radius(10)
print(circle)
