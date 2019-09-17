#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

print('Creating a dictionary with dict')
d = dict(One = 1, Two = 2, Three = 3, Four = 4, Five = 5)
print(d)
print(type(d))

print('Printing dictionary with loop')
for i in d:
    print(i, end = ' ', flush = True)
print()

print('Printing both key and values of dictionary with loop')
for k,v in d.items() :
    print('{} : {}'.format(k,v))
