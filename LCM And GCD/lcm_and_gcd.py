from math import gcd

def get_lcm_and_gcd(a,b):
	the_gcd = gcd(a,b)
	the_lcm = a * b / the_gcd
	return str(int(the_lcm)) + " " + str(the_gcd)
# test the function

print (get_lcm_and_gcd(5,10))
print (get_lcm_and_gcd(14,8))