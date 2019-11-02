def palindrome(n):
	stringn = str(n)
	listn = list(stringn)
	sumn = 0
	
	for i in listn:
		sumn += int(i)
	
	listsumn = list(str(sumn))
	if len(listsumn) == 1:
		return "Yes"
	if listsumn[0] == listsumn[1]:
		return "Yes"
	else:
		return "No"



# test the function

print (palindrome(56))
print (palindrome(1))
print (palindrome(98))
print (palindrome(999))