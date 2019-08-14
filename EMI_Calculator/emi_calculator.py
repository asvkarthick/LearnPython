#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

def emi(p, r, n):
    e = p * r * pow(1 + r, n) / (pow(1 + r, n) - 1)
    return e

# Principal
p = 2800000
# Rate of interest
r = 12 / 100.0
# Number of months
n = 15 * 12

print('Principal = ', p)
print('Rate of interest = ', r * 100)
print('Number of years = ', n / 12)
print('EMI = ', emi(p, r / 12, n))
