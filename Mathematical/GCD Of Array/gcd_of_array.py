from functools import reduce
from math import gcd

def gcd_of_array(arr):
	return reduce(gcd,arr)

# test the function

print (gcd_of_array([5,10]))
print (gcd_of_array([1,7]))