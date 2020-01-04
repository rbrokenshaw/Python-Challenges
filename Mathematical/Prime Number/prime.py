def isPrime(n):
	if n > 1:
		for i in range(2,n):
			if n % i == 0:
				return "No"
			else:
				return "Yes"
	else:
		return "No"

# test the function

print (isPrime(5))
print (isPrime(6))
print (isPrime(7))
print (isPrime(8))
print (isPrime(97))