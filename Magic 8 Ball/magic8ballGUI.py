import tkinter as tk
import time
import random

answers = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes- definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now", "Cannot predict now.", "Concentrate and ask again", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

def start():
	root = tk.Tk()

	def refresh():
		root.destroy()
		start()

	def quit():
		root.destroy()

	def play_again():
		refresh()

	def ask_question():
		thinking_label = tk.Label(root, text="Thinking...")
		thinking_label.grid(row=5, column=0)
		time.sleep(3)
		answer = random.choice(answers)
		answer_label = tk.Label(root, text=f"The Magic 8 Ball says: {answer}")
		answer_label.grid(row=6, column=0)
		play_again_button = tk.Button(root, text="Play Again", command=play_again)
		play_again_button.grid(row=7, column=0)

	def clear():
		user_input.delete(0, tk.END)

	question_label = tk.Label(root, text="What would you like to ask the Magic 8 Ball?")
	question_label.grid(row=0, column=0)
	user_input = tk.Entry(root)
	user_input.grid(row=1, column=0)

	ask_button = tk.Button(root, text="Ask", command=ask_question)
	ask_button.grid(row=2, column=0)
	clear_button = tk.Button(root, text="Clear", command=clear)
	clear_button.grid(row=3, column=0)
	quit_button = tk.Button(root, text="Quit", command=quit)
	quit_button.grid(row=4, column=0)


	root.mainloop()

if __name__ == '__main__':
    start()








