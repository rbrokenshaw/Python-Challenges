def find(a,b,k):
	ab_sum = str(a ** b)
	print (ab_sum)
	return ab_sum[::-1][k-1]
	

# test the function

print (find(3,3,1))
print (find(5,2,2))
print (find(50,2,3))
