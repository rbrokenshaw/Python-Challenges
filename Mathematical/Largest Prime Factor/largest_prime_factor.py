#The factors of a number are numbers that evenly divide into it. A prime factor is a factor that is only divisible by 1 and itself. 

# needs optimising

def largestPrimeFactor(n):
	counter = n
	for i in range(n, 1, -1):
		if n % counter == 0 and n % n == 0 and counter != n:
			result = counter
			break
		counter -= 1

	return result


# test the function

print (largestPrimeFactor(6))
print (largestPrimeFactor(15))
