#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

def minimum(a, b, c):
    if a < b:
        if a < c:
            return a
        else:
            return c
    else:
        if b < c:
            return b
        else:
            return c

if __name__ == "__main__":
    print(minimum(1, 2, 3))
    print(minimum(2, 1, 3))
    print(minimum(3, 2, 1))
