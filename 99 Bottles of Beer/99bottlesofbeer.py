counter = 99

while counter > 2:
	print (f"{counter} bottles of beer on the wall, {counter} bottles of beer.")
	counter -= 1
	print (f"Take one down and pass it around, {counter} bottles of beer on the wall.\n")

if counter == 2:
	print (f"{counter} bottles of beer on the wall, {counter} bottles of beer.")
	counter -= 1
	print (f"Take one down and pass it around, {counter} bottle of beer on the wall.\n")

if counter == 1:
	print (f"{counter} bottle of beer on the wall, {counter} bottle of beer.")
	counter -= 1
	print (f"Take one down and pass it around, no more bottles of beer on the wall.\n")

if counter == 0:
	print (f"No bottles of beer on the wall, no bottles of beer.")
	counter += 99
	print (f"Go to the store and buy some more, {counter} bottles of beer on the wall.")