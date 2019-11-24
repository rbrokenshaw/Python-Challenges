def isPerfect(n):
	factor_list = []
	for i in range(1,n):
		if n % i == 0:
			factor_list.append(i)

	if sum(factor_list) == n:
		return 1
	else:
		return 0

# test the function

print (isPerfect(6))
print (isPerfect(21))
print (isPerfect(28))