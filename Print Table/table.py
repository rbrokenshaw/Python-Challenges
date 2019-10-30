def table(n):
	output_list = []
	for i in range(1,11):
		output_list.append(n * i)
	output = str(output_list).strip('[]')
	output = output.replace(",", "")
	return output


print(table(4))

'''
if __name__ == "__main__":
	t=int(input())
	for i in range(t):
		n = int(input())
		print (table(n))
'''