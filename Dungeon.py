
N = 0;

S = 0;

E = 0;

W = 0;


def Intro():

	print('''

It may have been something wrong with the treasure map, but how you got here
is not relevant. What is relevant is that you are lying on a stone cold surface
in the middle of nowhere, thousands of kilometers from home. On the wall you see a
bronze carving of a horrific demon, an Aztec figure. It may be a hallucination,
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

''')

	inputloop()


def inputloop():

	while True:

		global N

		global S

		global E

		global W

		direction = input("Which direction do you move?\n")

		if direction != "N" and direction != "S" and direction != "E" and direction != "W":

			print("Press E or W or N or S and press enter")

		elif direction == "N":

			N = N+1

			S = S-1

			print("\n\nWalking North...")

			break

		elif direction == "S":

			S = S+1

			N = N-1

			print("\n\nWalking South...")

			break

		elif direction == "E":

			E = E+1

			W = W-1

			print("\n\nWalking East...")

			break

		elif direction == "W":

			W = W+1

			E = E-1

			print("\n\nWalking West...")

			break

	Game()



def Game():

	global N

	global S

	global E

	global W

	if N > 0 and E == 0 and W == 0:

		print("You cannot go North; the bronze demon blocks the way.")

		N = 0

	if N > 3:

		N = 3

		S = -3

		print("You cannot go further North.")

	elif S > 3:

		S = 3

		N = -3

		print("You cannot go further South.")

	elif E > 3:

		E = 3

		W = -3

		print("You cannot go further East")

	elif W > 3:

		W = 3

		E = -3

		print("You cannot go further West")

	print("\nPosition:")

	print("North:",str(N))

	print("South:",str(W))

	print("East:",str(E))

	print("West:",str(S))

	inputloop()



# Functions Instantiated Here:

Intro()








