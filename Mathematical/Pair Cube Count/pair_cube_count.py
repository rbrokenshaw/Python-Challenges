def pairCubeCount(n):
	count = 0

	for a in range(0,n):
		for b in range(1,n):
			if a ** 3 + b ** 3 == n:
				count += 1

	return count

# test the function

print (pairCubeCount(9))
print (pairCubeCount(28))