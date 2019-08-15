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

    def dot(self, v):
        new_coordinates = [x * y for x,y in zip(self.coordinates, v.coordinates)]
        result = sum(new_coordinates)
        return result

    def angle(self, v):
        dot_product = self.dot(v)
        mag1 = self.magnitude()
        mag2 = v.magnitude()
        return math.acos(dot_product / (mag1 * mag2)) * 180 / math.pi

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

v1 = Vector([7.887, 4.138])
v2 = Vector([-8.802, 6.776])
print('dot = ', v1.dot(v2))

v1 = Vector([-5.955, -4.904, -1.874])
v2 = Vector([-4.496, -8.755, 7.103])
print('dot = ', v1.dot(v2))

v1 = Vector([3.183, -7.627])
v2 = Vector([-2.668, 5.319])
print('Angle = ', v1.angle(v2))

v1 = Vector([7.35, 0.221, 5.188])
v2 = Vector([2.751, 8.259, 3.985])
print('Angle = ', v1.angle(v2))

v1 = Vector([-7.579, -7.88])
v2 = Vector([22.737, 23.64])
print('Angle = ', v1.angle(v2))

v1 = Vector([-2.029, 9.92, 4.172])
v2 = Vector([-9.231, -6.639, -7.245])
print('Angle = ', v1.angle(v2))

v1 = Vector([-2.328, -7.284, -1.214])
v2 = Vector([-1.821, 1.072, -2.94])
print('Angle = ', v1.angle(v2))
