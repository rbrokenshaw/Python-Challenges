def divisors(n):
	if n >= 4:
		outerCount = 0
		for i in range(4,n):
			innerCount = 1
			for x in range(1,int(i/2) + 1):
				if i % x == 0:
					innerCount += 1
			if innerCount == 3:
				outerCount += 1
		return outerCount
	else:
		return 0

# test the function

print (divisors(6))
print (divisors(10))
print (divisors(30))