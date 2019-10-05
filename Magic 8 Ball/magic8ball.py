import time
import random

answers = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes- definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now", "Cannot predict now.", "Concentrate and ask again", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

user_question = input("What would you like to ask the Magic 8 Ball?\n") 
print(f"You asked: {user_question}")
print("Thinking...")
time.sleep(3)
print ("Magic 8 Ball's response: '" + random.choice(answers) + "'")








