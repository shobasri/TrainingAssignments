#!/usr/bin/python

import sys

a=int(sys.argv[1])

for k in range(0,(a+1)):
	b=k%2
	if b==1:
		print (k)
