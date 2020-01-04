from math import factorial

def npr(n,r):
	if n == 0:
		return 1
	else:
		return int((factorial(n)) / factorial(n - r))

# test the function


print(npr(0,1))
print(npr(2,1))
print(npr(10,4))