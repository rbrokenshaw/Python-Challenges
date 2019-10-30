def printPat(n):
	counter = n
	string_list = []
	repetition = n
	for i in range(counter, 0, -1):
		for i in range(counter, 0, -1):
			string_list.append((str(i) + " ") * repetition)
		repetition -= 1
		string_list.append("$")

	sep = ""
	return_string = sep.join(string_list)
	return return_string

print (printPat(2))