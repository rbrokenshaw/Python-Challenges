import itertools

def primePairs(n):
	if n >= 4:
		# find all prime numbers between 2 and n
		multiples = []
		primeNums = []
		for i in range(2, n+1):
			if i not in multiples:
				primeNums.append(i)
				for x in range(i*i, n+1, i):
					multiples.append(x)
					
		# find all pairs that meet constraint
		pairs = []
		for p in primeNums:
			for q in primeNums:
				if p*q <= n:
					pairs.append(p)
					pairs.append(q)
		return " ".join(str(x) for x in pairs)
	else:
		return 0

# test the function

print (primePairs(4))
print (primePairs(8))
