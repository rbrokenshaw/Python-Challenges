# function to check if number contains two or more digits
def two_or_more_digits(n):
	num_list = (list(str(n)))
	if len(num_list) >= 2:
		return True

# function for checking for prime number
def is_prime(n):
	if n > 1:
		for i in range(2,n):
			if (n % i) == 0:
				return False
				break
		else:
			return True
	else:
		return False

# function to check if number contains 1 or 7
def contains_one_or_seven(n):
	if '1' in str(n) or '7' in str(n):
		return False
	else:
		return True

# function to check if sum of all digits is less than or equal to 10
def sum_less_than_or_equal_to_ten(n):
	num_list = (list(str(n)))
	total = sum(int(i) for i in num_list)
	if total <= 10:
		return True

# function to check if the sum of the first two digits is odd
def sum_first_two_digits_odd(n):
	num_list = (list(str(n)))
	if len(num_list) >= 2:
		if (int(num_list[0]) + (int(num_list[1]))) % 2 != 0:
			return True
	else: 
		return False

# function to check if the last but one digit is even
def last_but_one_digit_even(n):
	num_list = (list(str(n)))
	if (int(num_list[-2]) % 2 == 0) and (int(num_list[-2]) != 0):
		return True

# function to check if the last digit equals the number length
def last_digit_equals_length(n):
	num_list = (list(str(n)))
	if int(num_list[-1]) == len( num_list):
		return True

# create the list of numbers
number_list = [x for x in range(1,1001)]

# remove numbers of 2 digits or more
number_list = [n for n in number_list if two_or_more_digits(n)]
# keep only prime numbers
number_list = [n for n in number_list if is_prime(n)]
# remove numbers that contain '1' or '7'
number_list = [n for n in number_list if contains_one_or_seven(n)]
# check if sum of all digits is less than or equal to 10
number_list = [n for n in number_list if sum_less_than_or_equal_to_ten(n)]
# check if sum of first two digits is an odd number
number_list = [n for n in number_list if sum_first_two_digits_odd(n)]
# check if last digit is even
number_list = [n for n in number_list if last_but_one_digit_even(n)]
# check if last digit equals length of number
number_list = [n for n in number_list if last_digit_equals_length(n)]

# print the number
for i in number_list:
	print ("The number is: " + str(i))