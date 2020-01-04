another_order = 'Y'

while another_order == 'Y':
	def split(order):
		return [char for char in order]

	# create dictionary of menu
	menu = {'1': ['Chicken Strips', 3.50], '2': ['French Fries', 2.50], '3': ['Hamburger', 4], '4': ['Hotdog', 3.50], '5': ['Large Drink', 1.75], '6': ['Medium Drink', 1.50], '7': ['Milk Shake', 2.25], '8': ['Salad', 3.75], '9': ['Small Drink', 1.25]}

	# print the menu
	print ("Welcome to the menu calculator, here is the menu:")
	for key, value in menu.items():
		print ("\t" + key + " - " + value[0] + " - " + str(value[1]))

	# order input from user
	order = raw_input("Please enter the menu number of each item ordered without spaces:")
	order = order.replace(" ", "")

	# split the input order into list and create list of unique orders
	order_list = split(order)
	order_list_condensed = []

	for i in order_list:
		if i not in order_list_condensed:
			order_list_condensed.append(i)

	total = 0

	for i in order_list:
		total += menu[i][1]

	print ("You have ordered: ")
	for i in order_list_condensed:
		item = menu[i][0]
		quantity = order_list.count(i)
		print ("\t" + str(quantity) + " " + item)

	print ("And the total is: " + str(total))
	another_order = (raw_input("Would you like to calculate another order? Y/N:")).upper()




