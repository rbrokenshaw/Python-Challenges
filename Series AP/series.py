def series(a, b, int):
	pattern = b - a
	pattern_list = []
	start = a
	pattern_list.append(start)
	for i in range(int - 1):
		pattern_list.append(start + pattern)
		start += pattern

	return pattern_list[-1]

# test the function

print (series(2,3,4))
print (series(1,2,10))
