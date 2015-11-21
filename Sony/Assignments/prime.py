a = input("Enter a number: ")

for i in range(2,a):
	if (a%i == 0):
		break
if (i == a-1):
	print a,"is prime"
else:
	print a, "is NOT prime"