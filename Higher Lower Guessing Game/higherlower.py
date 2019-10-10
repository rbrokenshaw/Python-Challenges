import random

if __name__ == "__main__":
	play_again = 'Y'

	while play_again == 'Y':
		number = random.randint(1, 101)
		guessed = 'N'
		guess_count = 1

		print ("Welcome to the number guessing game! I am thinking of a number, can you guess what it is?")

		while guessed == "N":
			guess = input("Please guess a number: ")

			if int(guess) == number:
				print (f"Congratulations, you correctly guessed the number in {guess_count} tries!")
				guessed = "Y"
				play_again = input("Would you like to play again? (Y/N)").upper()
			elif int(guess) > number:
				guess_count += 1
				print ("Lower...")
			else:
				guess_count += 1
				print ("Higher...")