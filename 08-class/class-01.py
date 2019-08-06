#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

class Circle(object):
    def __init__(self, radius):
        self.radius = radius;

    def print_radius(self):
        print(self.radius)

circle = Circle(5)
circle.print_radius()
