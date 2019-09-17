#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>
# Function with variable number of arguments

def print_args(*args):
	if len(args):
		for i in args:
			print(i);
	else:
		print('No arguments passed')

print_args(1, 2, 3)
