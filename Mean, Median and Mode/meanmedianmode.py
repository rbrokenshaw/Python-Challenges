def calculate_mean(float_number_list, decimal_places):
	total = 0
	for i in number_list:
		total += float(i)
	mean = total / len(number_list)
	mean_return = (round(mean, int(decimal_places)))

	return ("The mean is " + str(mean_return))

def calculate_median(float_number_list):
	float_number_list = sorted(float_number_list, key=float)

	if len(float_number_list) % 2 == 0:
		value1 = int((len(float_number_list) / 2) - 1)
		value2 = int((len(float_number_list) / 2))

		median_list = ([float_number_list[value1], float_number_list[value2]])

		return ("The median numbers are " + str(median_list[0]) + " and " + str(median_list[1]) + " .")

	else:
		value1 = int((len(float_number_list) / 2))
		median = float_number_list[value1]

		return ("The median is " + str(median))

def calculate_mode(float_number_list):
	mode = max(set(float_number_list), key=float_number_list.count)

	return ("The mode is " + str(mode))


if __name__ == '__main__':
	user_input = input("Please enter your list of numbers separated by a comma: ")
	strip_whitespace = user_input.replace(" ", "")
	number_list = strip_whitespace.split(",")
	float_number_list = []

	for i in number_list:
		float_number_list.append(float(i))

	decimal_places = input("To how many decimal places would you like to round up the mean?")

	print (calculate_mean(float_number_list, decimal_places))
	print (calculate_median(float_number_list))
	print (calculate_mode(float_number_list))
