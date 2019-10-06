def checker():
	# user inputs three numbers
	side1 = input("Please enter the first value: ")
	side2 = input("Please enter the second value: ")
	side3 = input("Please enter the third value: ")

	# make a list of numbers and sort list by value
	side_list = [float(side1), float(side2), float(side3)]
	side_list.sort()

	# formula for pythagorean triple is a*a + b*b = c*c
	a_squared = side_list[0] * side_list[0]
	b_squared = side_list[1] * side_list[1]
	c_squared = side_list[2] * side_list[2]

	if (a_squared + b_squared) == c_squared and (c_squared.is_integer()):
		print ("Your triangle is a Pythagorean Triple!")
	else:
		print ("Your triangle is not a Pythagorean Triple!")

check = 'Y'

while check == 'Y':
	checker()
	
	# prompt to try again
	check = input("Would you like to try again? Enter Y/N: ")




