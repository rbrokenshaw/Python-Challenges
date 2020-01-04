def sieve(n):
	if n > 1:
		multipleList = []
		primeList = []
		for i in range(2,n+1):
			if i not in multipleList:
				primeList.append(i)
				for x in range(i*2, n+1, i):
					multipleList.append(x)
		return "The prime numbers up to or equal to " + str(n) + " are: " + " ".join(str(i) for i in primeList)
	else:
		return "There are no prime numbers up to or equal to " + str(n)

# test the function

print (sieve(10))
print (sieve(35))
