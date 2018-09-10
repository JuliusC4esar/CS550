word = "king"

print("Greetings, mortal!\n")
print("What is your name?\n")
name = input()
print("\nI am pleased to make your acquaintance, " + name + "!")
print('''
How about we play a game?

I am thinking of a four letter word. Can you guess it? 

(Please type in all lower case)
''')
for i in range(20):
	print("You have " + str(20-i) + " guesses left.")
	guess = input()
	if len(guess) == 4:
		rightletter = 0
		for x in range(4):
			if guess[x] == word[x]:
				rightletter = rightletter + 1
		if rightletter == 4:

			print("Congratulations, " + name + "! You have beaten me in the game! The word was king!")

			print("\nIt was a pleasure to meet you! Now, good day.\n")

			quit()

		print("You got " + str(rightletter) + " right letters in the correct spot")

	else:
		print("Please write a four letter word")

print("\nGuesses are depleted! Haha! I have won, " + name + "! But don't be disheartened, I'm sure you will beat me someday.")
print("\nBy the way, the word was " + word + ".")
print("\nIt was a pleasure to meet you! Now, good day.\n")




