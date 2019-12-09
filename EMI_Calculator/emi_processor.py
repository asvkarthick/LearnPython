#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

def emi(p, r, n):
    e = p * r * pow(1 + r, n) / (pow(1 + r, n) - 1)
    return e

def compute_interest(p, r):
    interest = p * r
    return interest

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

print('-----------------------------------------------------------------------------------------------------')
print('Month\t EMI\t\t\t Interest\t\t Principal\t\t Loan Balance')
print('-----------------------------------------------------------------------------------------------------')
i = 0
monthly_emi = emi(p, r, n)
principal_balance = p
while i < n:
    i = i + 1
    monthly_interest = compute_interest(principal_balance, r)
    monthly_principal = monthly_emi - monthly_interest
    principal_balance = principal_balance - monthly_principal
    print(i, '\t', monthly_emi, '\t', monthly_interest, '\t', monthly_principal, '\t', principal_balance)

print()
print()
print('Principal = ', p)
print('Rate of interest = ', r * 100.0 * 12.0)
print('Number of years = ', n / 12)
print('EMI = ', emi(p, r, n))
print('Total payment = ', n * emi(p, r, n))
print('Total interest paid = ', n * emi(p, r, n) - p)
