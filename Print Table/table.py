def table(n):
	for i in range(1,11):
		print (n * i, end=" ")

if __name__ == "__main__":
	t=int(input())
	for i in range(t):
		n = int(input())
		print (table(n))