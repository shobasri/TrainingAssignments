#!/usr/bin/python

import sys

a=int(sys.argv[1])

for k in range(2,a):
	for i in range(2,k):
		b = k%i
		if b==0:
			break
	else:
		print (k)
