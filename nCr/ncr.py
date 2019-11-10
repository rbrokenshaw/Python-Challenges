from math import factorial

def ncr(n,r):
	if n == 0:
		return 1
	else:
		return int((factorial(n)) / factorial(r) / factorial(n-r))

# test the function

print (ncr(3,2))
print (ncr(4,2))