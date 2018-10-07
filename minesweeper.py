# Kai
# October 2, 2018
# Functional minesweeper board generation
# Enter 3 integers: a width, a height, and a number of bombs, and a minesweeper board will be generated.


def zero():

	for x in range(height):

		for y in range(width-1):

			if hidden[x][y] == 0:

				if x+1 < height:

					hidden[x+1][y] = board[x+1][y]

					if hidden[x+1][y] == 0:

						zero() 	

				if x-1 >= 0:

					hidden[x-1][y] = board[x-1][y]

					if hidden[x-1][y] == 0:

						zero()

				if x+1 < height and y+1 < width:

					hidden[x+1][y+1] = board[x+1][y+1]

					if hidden[x+1][y+1] == 0:

						zero()

				if x-1 >= 0 and y+1 < width:

					hidden[x-1][y+1] = board[x-1][y+1]

					if hidden[x-1][y+1] == 0:

						zero()

				if x-1 >= 0 and y-1 >= 0:

					hidden[x-1][y-1] = board[x-1][y-1]

					if hidden[x-1][y-1] == 0:

						zero()

				if y+1 < width:

					hidden[x][y+1] = board[x][y+1]

					if hidden[x][y+1] == 0:

						zero()

				if y-1 >= 0:

					hidden[x][y-1] = board[x][y-1]

					if hidden[x][y-1] == 0:

						zero()

				if x+1 < height and y-1 >= 0:

					hidden[x+1][y-1] = board[x+1][y-1]

					if hidden[x+1][y-1] == 0:

						zero()














# Board generation starts here:

import random

import sys

try:

	width = int(sys.argv[1])

	height = int(sys.argv[2])

	bombs = int(sys.argv[3])


	if width*height >= 25 and width*height >= bombs:

		board = [[0] for x in range(height)]

		
		for x in range(height):

			for y in range(width-1):

				board[x].append(0)


		hidden = [['?'] for x in range(height)]

		for x in range(height):

			for y in range(width-1):

				hidden[x].append('?')






		b = 0         # Number generation and bomb generation

		while b < bombs:    

			x = random.randint(0,height-1)

			y = random.randint(0,width-1)

			if board[x][y] != '*':

				board[x][y] = '*'

				if x+1 < height:

					if board[x+1][y] != '*':
				
						board[x+1][y] += 1

				if x-1 >= 0:

					if board[x-1][y] != '*':

						board[x-1][y] += 1

				if x+1 < height and y+1 < width:

					if board[x+1][y+1] != '*':

						board[x+1][y+1] += 1

				if x-1 >= 0 and y+1 < width:

					if board[x-1][y+1] != '*':

						board[x-1][y+1] += 1

				if x-1 >= 0 and y-1 >= 0:

					if board[x-1][y-1] != '*':

						board[x-1][y-1] += 1

				if y+1 < width:

					if board[x][y+1] != '*':

						board[x][y+1] += 1

				if y-1 >= 0:

					if board[x][y-1] != '*':

						board[x][y-1] += 1

				if x+1 < height and y-1 >= 0:

					if board[x+1][y-1] != '*':

						board[x+1][y-1] += 1

			elif board[x][y] == '*':

				b = b-1

			b = b + 1



			

			# Initial Reveal

			initialx = int(width/2)

			initialy = int(height/2)

			hidden[initialy][initialx] = board[initialy][initialx]

			hidden[initialy+1][initialx] = board[initialy+1][initialx]

			hidden[initialy-1][initialx] = board[initialy-1][initialx]

			hidden[initialy][initialx+1] = board[initialy][initialx+1]

			hidden[initialy][initialx-1] = board[initialy][initialx-1]




		print()  # Print final board

		for x in range(height):

			print(*hidden[x])









		# Input starts here:


		while True:

				while True:

					try:

						xpos = int(input("\nEnter the x-coordinate of the region that you wish to reveal.\n"))

						ypos = int(input("\nEnter the y-coordinate of the region that you wish to reveal.\n"))

						if xpos >= 0 and xpos <= width and ypos >= 0 and ypos <= height:

							break

						else:

							print("That number doesn't work! Select a proper one, yeah?")

					except ValueError:

						print("\nThat number doesn't work! Select a proper one, yeah?\n")




				if board[ypos][xpos] == '*': # Lose

					print("\nYou selected a mine! You lose! Here are all the positions of the mines!")

					for x in range(height):

						for y in range(width):

							if board[x][y] == '*':

								hidden[x][y] = board[x][y]


					for x in range(height): # Print board

						print(*board[x])



					quit()



				else:

					print("\nYou landed on the number:",board[ypos][xpos])

					hidden[ypos][xpos] = board[ypos][xpos]

					if hidden[ypos][xpos] == 0:

						zero()

				for x in range(height): # Print board

					print(*hidden[x])


				if board.count('*') == hidden.count('?'): # Win condition

					print("\nYou have cleared the board! You win!")

					quit()



	else:  # Max bomb limit

		print("\nThis number of bombs does not work with the board size. You cannot have",bombs,"bombs with",str(width*height),"square units board size!")

		quit()

except ValueError: # Enter three integers into the console

	print("\nPlease enter 3 integers: A width, a height, and a number of bombs.")

	quit()












