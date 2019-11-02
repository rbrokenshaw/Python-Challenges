def armstrong(n):
	nstring = str(n)
	nlist = list(nstring)
	result = 0
	for i in nlist:
		result += int(i)**3
	
	if result == n:
		return "Yes"
	else:
		return "No"

# test the function

print (armstrong(1))
print (armstrong(153))
print (armstrong(371))
print (armstrong(692))