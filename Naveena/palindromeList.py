#!/usr/bin/python

import sys

a=sys.argv[1]

b=a[::-1]

if a == b:
	print (a,"is a palindrome")
else:
	print (a, "is not a palindrome")
