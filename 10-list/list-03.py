#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

print('Create a list')
l = [1, 2, 3, 4, 5]
print(l)

print('Append 6 to the list')
l.append(6)
print(l)

print('Insert 100 to the beginning of the list')
l.insert(0, 100)
print(l)

print('Remove the last element from the list')
l.pop()
print(l)

print('Removing element at index 1')
l.remove(1)
print(l)

print('Remove element at index 2')
del l[2]
print(l)
