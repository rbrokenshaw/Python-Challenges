def jumping(n):
	number_list = []
	for i in range(0,n+1):
		if len(str(i)) == 1:
			number_list.append(str(i))
		else:
			nlist = list(str(i))
			for x in nlist:
				if int(x) == int(nlist[0]) + 1 or int(x) == int(nlist[0]) -1:
					number_list.append(str(i))
	return " ".join(number_list)

# test the function

print (jumping(10))
print (jumping(50))