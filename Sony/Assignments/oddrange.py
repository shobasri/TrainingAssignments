#print odd no in a range

a= input("Enter first no ")
b= input("Enter second no ")
for i in range(a,b):
	if (i%2!=0):
		print i, "is odd number"