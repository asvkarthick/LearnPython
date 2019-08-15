#!/usr/bin/python
# Karthick Kumaran <asvkarthick@gmail.com>

import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def sub(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def scale(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def div(self, c):
        new_coordinates = [x / c for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        mag = 0.0
        for x in self.coordinates:
            mag += x * x
        return math.sqrt(mag)

    def normalize(self):
        return self.div(self.magnitude())

v1 = Vector([1, 2])
print v1

v1 = Vector([8.218, -9.341])
v2 = Vector([-1.129, 2.111])
print v1
print v2
print v1.add(v2)
print v1.sub(v2)
print v1.scale(10)

v1 = Vector([-0.221, 7.437])
v2 = Vector([8.813, -1.331, -6.247])
v3 = Vector([5.581, -2.136])
v4 = Vector([1.996, 3.108, -4.554])
print v1.magnitude()
print v2.magnitude()
print v3.magnitude()
print v4.magnitude()

v3 = v3.div(v3.magnitude())
v4 = v4.div(v4.magnitude())
print v3
print v4
print v1.normalize()
