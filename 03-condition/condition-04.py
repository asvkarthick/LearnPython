#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

x = True
y = True if x is True else False

print(x)
print(y)

n = 20
odd_even = 'Even' if n % 2 == 0 else 'Odd'
print(odd_even)
