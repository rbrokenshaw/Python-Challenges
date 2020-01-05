import math

def countSquares(n):
	counter = 0
	for i in range(1, n):
		root = math.sqrt(i)
		if int(root + 0.5) ** 2 == i:
			counter += 1
	return counter

# test the function


print (countSquares(9))
print (countSquares(3))
