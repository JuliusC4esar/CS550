# Kai 
# Sept. 24, 2018
# Text Aventure. Explore the ancient dungeon and escape! There are many ways to die, but keep in mind that there is indeed one way to escape the dungeon alive. The game is not impossible.
# Sources:
# https://www.programiz.com/python-programming/global-local-nonlocal-variables
# https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
# On my honor, I have neither given nor received unauthorised aid.


# Initial description:

def Intro():

	global N
	global S
	global E
	global W
	global chestkey
	global sword
	global man
	global holykey

	chestkey = False

	holykey = False

	sword = False

	man = True

	N = 0

	S = 0

	E = 0

	W = 0

	print('''

It may have been something wrong with the treasure map, but how you got here
is not relevant. What is relevant is that you are lying on a stone cold surface
in the middle of nowhere, thousands of kilometers from home. On the wall you see a
bronze statue of a horrific demon, an Aztec figure. It may be a hallucination,
but you suddenly see the mouth of the bronze carving move, as if it is trying to 
croak out a sentence. Suddenly, barely audible words are heard:

"If you wish to pass and earn your freedom, you must locate the holy key.
Come and bring it to me, and I shall show you the path of the exit."

You stand up. It may be the immense hunger in your stomach or your insatiable
appetite for adventure, but you decide to take the word of the bronze demon
and begin the search for the holy key. 

Controls:

Press E and enter to walk East.

Press W and enter to walk West.

Press S and enter to walk South.

Press N and enter to walk North.

Press I to interact.

''')

	inputloop()










# Movement:

def inputloop():

	while True:  # Repeat until proper input is given

		global N

		global S

		global E

		global W

		direction = input("\nDo you interact or do you move?\n")

		# Get input command and initialize response. Break loop when proper input is received.

		if direction.lower() == "n":

			N = N+1

			S = S-1

			print("\n\n\n\n\nWalking North...")

			break

		elif direction.lower() == "s":

			S = S+1

			N = N-1

			print("\n\n\n\n\nWalking South...")

			break

		elif direction.lower() == "e":

			E = E+1

			W = W-1

			print("\n\n\n\n\nWalking East...")

			break

		elif direction.lower() == "w":

			W = W+1

			E = E-1

			print("\n\n\n\n\nWalking West...")

			break

		elif direction.lower() == "i":

			interactions()  # Interactions void

		else:

			print("Typing error. Please press E or W or N or S or I and press enter.")

	Game()










# Room Correspondance to Movement:

def Game():

	global N

	global S

	global E

	global W

	# Movement limit:

	if N > 1:

		N = 1

		S = -1

		print("\n\nYou cannot go further North.")

	elif S > 1:

		S = 1

		N = -1

		print("\n\nYou cannot go further South.")

	elif E > 1:

		E = 1

		W = -1

		print("\n\nYou cannot go further East")

	elif W > 1:

		W = 1

		E = -1

		print("\n\nYou cannot go further West")


	# Show position:

	print("\nPosition:")

	print("North:",str(N))

	print("South:",str(S))

	print("East:",str(E))

	print("West:",str(W))


	# Room descriptions:

	if N == 0 and S == 0 and E == 0 and W == 0:

		centralroom()

	elif N == 1 and E == 0 and W == 0:

		above()

	elif N == 1 and W == 1:

		abovewest()

	elif N == 1 and E == 1:

		aboveeast()

	elif N == 0 and E == 1:

		east()

	elif N == 0 and W == 1:

		west()

	elif S == 1 and W == 1:

		belowwest()

	elif S == 1 and E == 1:

		beloweast()

	elif S == 1 and E == 0 and W == 0:

		below()

	inputloop() # Repeat input loop when functions are completed









# Interaction caller:

def interactions():

	global N

	global S

	global E

	global W

	if N == 1 and E == 0 and W == 0:

		interactAbove()

	elif N == 1 and W == 1:

		interactAboveWest()

	elif N == 0 and W == 0:

		interactCentral()

	elif N == 0 and E == 1:

		interactEast()

	elif N == 0 and W == 1:

		interactWest()

	elif S == 1 and E == 1:

		interactSouthEast()

	elif N == 1 and E == 1:

		interactAboveEast()

	elif S == 1 and E == 0:

		interactBelow()

	elif S == 1 and W == 1:

		interactBelowWest()

	else:

		print("\nYou cannot interact with anything in this room.")










# Room Descriptions Here:


def centralroom():

	print("\nYou are in the central room. A horrific bronze demon stares at you.")









def above():

	print("\nYou enter a dark chamber. A golden trap door lies on the ground. Next to it sits a lever.")








def abovewest():

	print('''
You enter a room with magnificent golden walls. Engraved on the walls lies a riddle.

"What gets wet as it dries?"
''')








def aboveeast():

	print("You enter a poorly lit room. There is a carving on the wall of a bird with an open mouth.")








def east():

	print("You enter a room with a locked treasure chest. Do you have a key...?")








def beloweast():

	if man:

		print('''
You walk into a dark room and you are startled by a sudden echo in the chamber.

"Can you guess the Word of Virtue? Guess correctly, and I shall grant you the Holy Key. Guess incorrectly, and you shall perish."
		''')

	else:

		print("You enter the room that you killed the old man in the black robes in. On the ground lies his corpse.")










def below():

	print('''
You enter a room and you are shocked to find a bronze key sitting on a golden platform!

Is it perhaps the Holy Key that the bronze demon spoke of?
''')








def belowwest():

	print('''
As soon as you enter the South West room, you are instantly terrified by the sheer darkness of the chamber.
It may have been an arrow, but you suddenly hear a mysterious projectile fly past your head.

You do not know if you should explore the room or back away.
		''')








def west():

	print('''
A grand gate sits in front of you. Is it an exit?
It appears to have a keyhole. Do you have a key?
		''')













# Interaction Functions Here:


def interactAbove():

	print('''
You may not have thought your entire plan through, but something about
interacting with a trap door didn't seem wise.
Nonetheless, out of desperation to escape you stand on the trap door and
pull the lever next to it.

You fall to your death.

THE END.
		''')

	quit()











def interactAboveWest():

	print("You approach the riddle. What is your answer?\n")

	answer = input("Answer: ")

	if answer.lower() == "towel":

		global chestkey

		chestkey = True

		print("\nYou have answered correctly! A rusty silver key appears in front of you. Thrilled, you grab it.")

	else:

		print('''
You have answered incorrectly! You suddenly hear a loud banging noise in the ceiling.
What could it be? You soon realize that your death is imminent and think your final thoughts
as you are crushed to death by numerous boulders.

THE END.
''')

		quit()










def interactCentral():

	global chestkey

	if holykey:

		print('''
Trembling, you hand the Holy Key over to the bronze demon. The demon laughs.
"Good... you have done well," the demon growls. "And now... you shall die!"
You are shocked at the betrayal of the demon, but shock will not aid you in this dire situation.
The demon slashes at you with its claws and you fall to the ground.

THE END.
			''')

		quit()

	elif chestkey:

		print('''
The bronze demon growls.
"What is this?" it shrieks. "A rusty silver key? I demanded the Holy Key! Do not waste my time, fool!"

Terrified, you back away.
''')

	else:

		print("You do not have the Holy Key to give to the bronze demon. Find it and then return.")










def interactEast():

	global chestkey

	global sword

	if chestkey:

		sword = True

		print('''
You use the rusty silver key that you acquired from the riddle to open the chest.
Your heart pounds as you lift open the golden treasure chest lid. You reach in...

You found an old and rusty Inca Sword! As you examine the blade, you notice that
an ancient script is engraved on the bronze.

What does it mean? This will perhaps forever remain a mystery to you.

You decide to keep the sword.
''')

	else:

		print("You do not have a key.")










def interactWest():

	global holykey

	if holykey:

		print('''
You use the golden Holy Key and unlock the gate. The golden gate's eerie creek is echoed throughout the halls.
Suddenly, you hear the bronze demon's voice. You are terrified to hear it say:

"Are you trying to leave, foolish mortal? I'm coming for you! Nobody escapes this dungeon!"

You hear the demon's footsteps coming closer and closer.

You begin to run. With each footstep of the demon you hear, you run faster and faster.

Your immense exhaustion is almost about to consume you when you suddenly see light.

The first light you have seen in days!

You sprint towards the source of light and jump through the crack.

You find yourself lying on a beach, the warming sun on your shoulders.

You have escaped. You have earned your freedom.

THE END.
''')

		quit()

	elif chestkey:

		print("The rusty silver key does not fit into the keyhole. Perhaps there is another key somewhere...")

	else:

		print("You do not have a key.")










def interactAboveEast():

	print('''
You approach the open mouthed bird, when suddenly you step on a pressure plate.
An arrow is shot from the bird's mouth and strikes you in the leg.

You fall to the ground and bleed to death.

THE END.
''')

	quit()









def interactBelow():

	print('''
You approach the bronze key and excitedly snatch it from its holder. 
You hear a sudden cracking in the ceiling. It's a trap!
You try to run out of the room but the exit is blocked off by a fallen boulder.

You are crushed to death.

THE END.
		''')

	quit()









def interactBelowWest():

	print('''
You decide to explore the dark chamber. Seconds later, you hear many more projectiles whizzing past your head.

Panicking, you try to find the exit of the chamber, but it is too dark.  

An arrow strikes your body and you fall.

THE END.
		''')

	quit()










def interactSouthEast():

	global man

	global holykey

	global sword

	if man:

		word = "light"

		print("You step closer, and you suddenly hear the voice boom:")

		print("\n'Step forward, mortal! Can you guess the Word of Virtue? It is five letters long! You have twenty guesses before your death!' the voice howls.\n")

		for i in range(20):

			print("You have " + str(20-i) + " guesses left.")

			guess = input()
			if len(guess) == 5:
				rightletter = 0
				for x in range(5):
					if guess[x].lower() == word[x].lower():
						rightletter = rightletter + 1
				if rightletter == 5:

					if sword == False:

						print('''
"Well done, mortal." the voice says. "You are the first in fifty years to guess the Word of Virtue correctly.
However, I am afraid I have a reputation to keep."

Suddenly, an old man in black robes appears before your very eyes, as if he had just faded into existence.

"Die, mortal!" he shrieks.

He unsheathes his sword and slashes at your stomach. Defenseless, you fall to the ground.

"Nobody faces me and lives," the old man says.

Your eyes close as you take your final breaths.

THE END.
							''')

						quit()

					if sword:

						print('''
"Well done, mortal." the voice says. "You are the first in fifty years to guess the Word of Virtue correctly.
However, I am afraid I have a reputation to keep."

Suddenly, an old man in black robes appears before your very eyes, as if he had just faded into existence.

"Die, mortal!" he shrieks.

He unsheathes his sword and prepares to slash, but as he lifts his sword you immediately unsheathe the Inca Sword 
that you had found in the treasure chest.

"Begone!" he says. 

As he thrusts forth his sword, you jump to the side and avoid his attack.

You then quickly force the Inca Sword into the back of the old man.

As he falls to the ground, you see a golden key fall out of his robes.

The Holy Key!

You snatch it and run.
							''')

						holykey = True

						man = False

						inputloop()

				print("\nYou guessed " + str(rightletter) + " right letters in the correct spot, mortal!")

			else:
				print("\nDo not waste my time, mortal. The Word of Virtue is five letters long!")

	else:

		print("You poke the corpse with your sword. Nothing happens.") 

		inputloop()

	print('''
You have failed to guess the Word of Virtue!

Suddenly, you see an old man in black robes appear before your very eyes.

He unsheathes a sword.

"You have failed, and now you must die!" he shrieks.

He brings his sword over your head and you fall to the ground.

Your eyes close as you take your final breaths.

THE END.
	''')	

	quit()






# Functions Instantiated Here:

Intro()








