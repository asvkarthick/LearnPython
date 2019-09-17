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

print('Printing only keys')
for k in d.keys() :
    print(k)

print('Printing only values')
for v in d.values() :
    print(v)

print('Printing with index')
print(d['Three'])

print('Updating dictionary with index')
d['Three'] = 300
print(d)

if 'One' in d :
    print('One is present in dictionary')
else :
    print('One is not present in dictionary')
