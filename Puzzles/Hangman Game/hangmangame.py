import random

def split(word):
	return [char for char in word]

words = ['python', 'java', 'javascript', 'ruby']
word_count = len(words)
random_number = random.randint(0, word_count - 1)
word = words[random_number]
letter_list = split(word)
underscore_list = []
guessed = 'N'
max_turns = 15
turns = 0

for i in letter_list:
	underscore_list.append("_")

print ("Welcome to the hangman game! I am thinking of a word, can you guess it? You have 15 tries!")
print ("You may give up at any time by typing '!'")


while guessed == 'N':
	if turns == max_turns:
		print ("You lose! The word was: " + word)
		guessed = 'FAILED'
	else:
		print ("The word: " + " ".join(underscore_list))
		letter = input("Guess a letter! ")

		if letter.isalpha():
			if letter in letter_list:
				for i in letter_list:
					if i == letter:
						letter_index = letter_list.index(i)
						letter_list[letter_index] = 0
						underscore_list[letter_index] = letter
						
				if '_' in underscore_list:
					print ("You found a letter! Guess another!")
					turns +=1
					print ("Turns taken: " + str(turns))
				else:
					print ("Congratulations, you win! The word was: " + word)
					guessed = 'Y'
			else:
				print ("Nope! Try again!")
				turns += 1
				print ("Turns taken: " + str(turns))
		else:
			if letter == '!':
				print ("You lose! The word was: " + word)
				guessed = 'FAILED'
			else:
				print ("Please enter a valid character!")





