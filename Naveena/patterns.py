#!/usr/bin/python

import sys

r=int(sys.argv[1])

n = 0

print ("Pattern B")
for x in range (0,(r+1)):
    n = n + 1
    for a in range (0, n-1):
        print ('*', end = '')
    print ()
print ('')

print ("Pattern A")
for b in range (0,(r+1)):
    n = n - 1
    for d in range (0, n+1):
        print ('*', end = '')
    print ()
print ('')

print ("Pattern D")
for e in range ((r+1),0,-1):
    print (((r+1)-e) * ' ' + e * '*')
print ('')

print ("Pattern C")
for g in range ((r+1),0,-1):
    print (g * ' ' + ((r+1)-g) * '*')
print ('')

print ("Patter E")
print ('')
for row in range(1,5):
    print (" " * (row -1) + row * "*" + (16 - row * 4) * " " + row * "*")
for row in range (0,4):
    print (" " * (3-row)+ "*" *(4 -row) + row * 4 * " " +"*" *(4 -row))

print ("Pattern F")
for f in range ((r+1),0,-1):
	print (f * ' ' + ((r+1)-f) * '* ')
print ('')

print ("Pattern H")
for h in range (0,(r+1)):
	print ((r-h) * ' ' + '*'.join([' ']*h))
print ('')

print ("Pattern I")
for i in range (0,(r+1)):
	print ((r-i) * ' ' + '*'.join(['*']*i))
print ((r-1) * ' ' + '*')
for i in range (1,(r-1)):
	print ((r-i) * ' ' + '*'.join(['*']*i))
print ('')
