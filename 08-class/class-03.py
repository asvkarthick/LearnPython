#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

class Circle(object):
    def __init__(self, radius):
        self.radius = radius;

    def print_radius(self):
        print(self.radius)

    def add_radius(self, r):
        self.radius += r

    def get_radius(self):
        return self.radius

def print_circle(obj) :
    print('Radius = {}'.format(obj.get_radius()))

circle = Circle(5)
circle.print_radius()
circle.add_radius(10)
circle.print_radius()

print_circle(circle)
