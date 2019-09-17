#!/usr/bin/python
# Author : Karthick Kumaran <asvkarthick@gmail.com>

def divide(num, den):
    try:
        res = num / den
    except ZeroDivisionError:
        print('Denominator is 0')
    else:
        return res

print(divide(6, 2))
print(divide(5, 0))
print(divide(100, 25))
