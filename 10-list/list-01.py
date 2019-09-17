#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

l = [1, 2, 3, 4, 5]
print(l)

l.append(6)
print(l)

l.insert(0, 0)
print(l)

print(type(l))

print('Print all the elements in the list with loop')
for i in l:
    print(i, end = ' ', flush = True)
print()
