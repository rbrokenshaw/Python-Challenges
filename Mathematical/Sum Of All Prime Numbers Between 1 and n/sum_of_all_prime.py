def sumOfAllPrime(n):
	if n > 1:
		multiples = []
		primeNums = []
		for i in range(2,n+1):
			if i not in multiples:
				primeNums.append(i)
				for x in range(i*i, n+1, i):
					multiples.append(x)
		return sum(primeNums)
	else:
		return 0


# test the function

print (sumOfAllPrime(5))
print (sumOfAllPrime(10))
print (sumOfAllPrime(0))