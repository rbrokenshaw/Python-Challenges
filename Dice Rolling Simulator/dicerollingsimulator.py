import random

if __name__ == '__main__':
	repeat = 'Y'

	while repeat == 'Y':
		# enter the number of sides on the dice
		sides = input("How many sides does your dice have?")
		while sides.isdigit() == False:
			sides = input("How many sides does your dice have? Please enter a number.")

		# enter the number of rolls
		rolls = input("How many times should we roll the dice?")
		while rolls.isdigit() == False:
			rolls = input("How many times should we roll the dice? Please enter a number.")

		# create list of random rolls
		number_list = []

		for i in range(int(rolls)):
			number = random.randint(1, int(sides))
			number_list.append(number)

		number_list.sort()

		# make list of unique numbers rolled
		condensed_number_list = []

		for i in number_list:
			if i not in condensed_number_list:
				condensed_number_list.append(i)

		# count number of times each number in unique rolls list is rolled
		for i in condensed_number_list:
			count = number_list.count(i)
			if count == 1:
				percentage = round((count / int(rolls)) * 100, 2)
				print (f"{i} was rolled once, and makes up {percentage}% of rolls.")
			elif count == 2:
				percentage = round((count / int(rolls)) * 100, 2)
				print (f"{i} was rolled twice, and makes up {percentage}% of rolls.")
			else:
				percentage = round((count / int(rolls)) * 100, 2)
				print (f"{i} was rolled {count} times, and makes up {percentage}% of rolls.")

		# ask the user if they would like to try again
		repeat = (input("Would you like to simulate another dice roll? Y/N")).upper()

