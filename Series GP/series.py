from math import floor

def series(a,b,int):
	pattern = b / a
	val = a
	pattern_list = []
	pattern_list.append(val)
	for i in range(int):
		result = val * pattern
		pattern_list.append(result)
		val += val
	return floor(pattern_list[int-1])

# test the function

print (series(2,3,1))
print (series(1,2,2))	