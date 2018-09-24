
# Functions:

def intro():

	name = str(input("\nGreetings, traveller. What is your name?\n"))

	print('''

You didn't think that it would ever be possible.

Up until this point, you were in heavy denial that you would ever reach such a destination.

Yet, now that you have witnessed for yourself the grand domes and buildings hanging over the city walls,

the gates of reality have suddenly opened.

Welcome,''',name+''', to the glorious ancient city of Xenloch.

	''')

	beginning()





def beginning():

	print('''

<BEGINNING>

As you enter the city walls, you cannot help but admire the glorious construction of the city facilities.

Xenloch is a city from a time when society was civilised, artistic, intelligent.

Now humanity has been reduced to a barbaric collection of endless wars, violence, and destruction.

Society has been destroyed almost to the extent of the ruins of Xenloch.

Xenloch, once a glorious and bustling city, now merely a collection of destroyed bricks and ancient buildings, barely standing.

As you walk into the abandoned city square, you suddenly hear a distant voice.

"Hello? Is anyone there?"

As you begin to walk away, you hear the voice again, louder this time.

"I have been waiting sixty years for you!"

You start to hear footsteps, but cannot deduct the source of them. Suddenly, an old man in white robes appears in front of you,

staring into your eyes.

"You have finally arrived!" he says. "The holy one has finally arrived!"

	''')

	dialogue1()





def dialogue1():

	print('''

[DIALOGUE OPTIONS]

'I am awfully confused, my good man. What relation could we have?' <press 1 and enter>

'What is the matter, crazed fool? Speak up!' <press 2 and enter>

	''')

	choice = int(input("Enter Your Choice:\n"))

	if choice == 1:

		choice1()

	elif choice == 2:

		choice2()

	else: 

		print("\nPlease enter 1 or 2")

		dialogue1()



def choice1:

	print("")


def choice2:

	print("Well, who ")



# Function Callings:

intro()







	