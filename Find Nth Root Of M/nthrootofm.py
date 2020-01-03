def nthRootOfM(n, m):
	solution = m**(1/n)
	if solution % 1 == 0:
		return solution
	else:
		return -1

# Test the function

print (nthRootOfM(2, 9))
print (nthRootOfM(3, 9))