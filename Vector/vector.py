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

v1 = Vector([1, 2])
print v1

v1 = Vector([8.218, -9.341])
v2 = Vector([-1.129, 2.111])
print v1
print v2
print v1.add(v2)
print v1.sub(v2)
print v1.scale(10)
