def reverse(n):
	nlist = list(str(n))
	nlist_string = "".join(nlist)
	nlist_string_reversed = nlist_string[::-1]
	return(int(nlist_string_reversed))

# test the function

print (reverse(2))
print (reverse(122))
print (reverse(12345))