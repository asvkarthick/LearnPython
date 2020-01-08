#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

import matplotlib.pyplot as plt

def emi(p, r, n):
    e = p * r * pow(1 + r, n) / (pow(1 + r, n) - 1)
    return e

def compute_interest(p, r):
    interest = p * r
    return interest

def print_emi_table(p, r, n):
    print('-----------------------------------------------------------------------------------------------------')
    print('Month\t     EMI\t Interest\t\t Principal\t\t Loan Balance')
    print('-----------------------------------------------------------------------------------------------------')
    i = 0
    monthly_emi = emi(p, r, n)
    principal_balance = p
    principal_greater_index = -1
    while i < n:
        i = i + 1
        monthly_interest = compute_interest(principal_balance, r)
        monthly_principal = monthly_emi - monthly_interest
        if principal_greater_index == -1:
            if monthly_principal > monthly_interest:
                principal_greater_index = i

        principal_balance = principal_balance - monthly_principal
        print('{:d}\t {:10.2f}\t {:10.2f}\t\t {:10.2f}\t\t {:10.2f}'.format(i, monthly_emi, monthly_interest, monthly_principal, principal_balance))

    return principal_greater_index

#### Start of Main ####
# Principal
p = int(input("Enter Principal:"))
# Rate of interest
r = float(input("Enter Rate of Interest(year):"))
r = r / 100.0 / 12.0 # Monthly interest
# Number of months
n = int(input("Enter number of years:"))
n = n * 12

print('Principal = ', p)
print('Rate of interest = ', r * 100.0 * 12.0)
print('Number of years = ', n / 12)
print('EMI = ', emi(p, r, n))
print('Total payment = ', n * emi(p, r, n))
print('Total interest paid = ', n * emi(p, r, n) - p)
print()
print()

principal_greater_index = print_emi_table(p, r, n)

print()
print()
print('Principal = ', p)
print('Rate of interest = {:0.3f}'.format(r * 100.0 * 12.0))
print('Number of years = ', n / 12)
print('EMI = {:0.2f}'.format(emi(p, r, n)))
print('Total payment = {:0.2f}'.format(n * emi(p, r, n)))
print('Total interest paid = {:0.2f}'.format(n * emi(p, r, n) - p))
print('Month Principal > Interest = {:d}'.format(principal_greater_index))
