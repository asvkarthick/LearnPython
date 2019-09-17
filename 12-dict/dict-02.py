#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

print('Creating a dictionary')
d = { 1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five' }
print(d)
print(type(d))

print('Printing dictionary with loop')
for i in d:
    print(i, end = ' ', flush = True)
print()

print('Printing both key and values of dictionary with loop')
for k,v in d.items() :
    print('{} : {}'.format(k,v))
