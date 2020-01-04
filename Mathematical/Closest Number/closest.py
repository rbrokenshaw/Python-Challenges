def closest(n,m):
	r1 = n%m
	r2 = n%-m
	if abs(r1) < abs(r2):
		return n - r1
	elif abs(r1) > abs(r2):
		return n - r2
	else:
		return n + r1 if abs(n+r1) > abs(n-r1) else n-r1

# test the function

print (closest(13,4))
print (closest(-15,6))
print (closest(221,-381))
print (closest(898,803))