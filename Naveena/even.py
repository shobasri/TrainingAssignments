#!/usr/bin/python

import sys

a=sys.argv[1]

b=int(a)%2

if b==0:
	print (a,"is a even number")
else:
	print (a,"is a odd number")
