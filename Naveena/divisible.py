#!/usr/bin/python

import sys

a=sys.argv[1]

b=int(a)%7

if b==0:
	print (a,"is perfectly divisible by 7")
else:
	print (a,"is not perfectly divisible by 7")
