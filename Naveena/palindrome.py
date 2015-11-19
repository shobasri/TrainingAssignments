#!/usr/bin/python

import sys

a=int(sys.argv[1])

b=a

i=0

while (b>0):
	i = (i * 10) + b % 10
	#print (i,b)
	b = int(b / 10)
	#print (b)

#print (a,i,b)

if (a == i):
	print (a,"is a palindrome")
else:
	print (a,"is not a palindrome")
