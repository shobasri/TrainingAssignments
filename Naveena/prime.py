#!/usr/bin/python

import sys

a=int(sys.argv[1])

if a > 1:
	for i in range(2,a):
		b = a%i
		if b==0:
			print (a,"is not a prime number")
			break
	else:
		print (a,"is a prime number")
else:
	print (a,"is not a prime number")
