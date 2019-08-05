#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

def what_number(x):
    if x == 0:
        print('x is zero')
    elif x > 0:
        print('x is positive number')
    else:
        print('x is negative number')

if __name__ == "__main__":
    a = 10
    b = 0
    c = -2

    what_number(a)
    what_number(b)
    what_number(c)
