# program to print list of even numbers with in a given range

a= input("Enter first no ")
b= input("Enter second no ")
for i in range(a,b):
	if (i%2==0):
		print i, "is even number"