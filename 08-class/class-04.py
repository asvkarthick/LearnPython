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

def print_circle(obj) :
    print('Radius = {}'.format(obj.radius()))

circle = Circle(5)
circle.print_radius()
circle.radius(10)
circle.print_radius()

print_circle(circle)
