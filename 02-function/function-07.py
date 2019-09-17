#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>
# This program has errors. See next program for the fix

def func1():
    func2()

def func2():
    print('This function is called from main')

if __name__ == '__main__':
    func1()
