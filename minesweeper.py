# Kai
# October 2, 2018
# Functional minesweeper board generation
# Enter 3 integers: a width, a height, and a number of bombs, and a minesweeper board will be generated.



winflag = 0



def zero():     # Reveal all adjacent tiles to each revealed zero in the board

	for y in range(height):

		for x in range(width-1):

			if hidden[y][x] == 0:

				if y+1 < height:

					hidden[y+1][x] = board[y+1][x]

				if y-1 >= 0:

					hidden[y-1][x] = board[y-1][x]

				if y+1 < height and x+1 < width:

					hidden[y+1][x+1] = board[y+1][x+1]

				if y-1 >= 0 and x+1 < width:

					hidden[y-1][x+1] = board[y-1][x+1]

				if y-1 >= 0 and x-1 >= 0:

					hidden[y-1][x-1] = board[y-1][x-1]

				if x+1 < width:

					hidden[y][x+1] = board[y][x+1]

				if x-1 >= 0:

					hidden[y][x-1] = board[y][x-1]

				if y+1 < height and x-1 >= 0:

					hidden[y+1][x-1] = board[y+1][x-1]

				














# Board generation starts here:

import random

import sys

try:

	width = int(sys.argv[1])

	height = int(sys.argv[2])

	bombs = int(sys.argv[3])


	horizontal = []

	line = []

	for x in range(width):

		horizontal.append(x)

		line.append('-')


	if width*height >= bombs and bombs >= 1:

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






		# Input starts here:


		while True:

			print('  ',*horizontal)
 
			print('  ',*line)

			for x in range(height): # Print board

				print((str(x)+'|'),*hidden[x])


			while True:

				pos = input("\nWhat do you want to do? Type in the x-coordinate followed by the y-coordinate followed by an m for mark or f for flag. Separate each with a comma. (x,y,m/f)\n")

				try:

					array = pos.split(',')

					xpos = int(array[0])

					ypos = int(array[1])

					action = array[2]

					if xpos >= 0 and xpos < width and ypos >= 0 and ypos < height and (action.lower() == 'm' or action.lower() == 'f'):

						break

					else:

						print("\nERROR: Either your coordinate values are out of range or your action is not an 'm' or an 'f'. Maybe you even made both of those mistakes. Separate all values with a comma.\n")

				except IndexError:

					print("\nERROR: Please enter the x value, the y value, and the action (m/f) separated by commas. Do not include parenthesis or spaces.\n")

				except ValueError:

					print("\nERROR: Please type in integers for the x and y values and an 'm' or an 'f' for the action. Follow this format: (x,y,m/f). Do not include parenthesis or spaces. Separate all values with a comma.\n")




			if board[ypos][xpos] == '*' and action.lower() == 'm': # Lose

				print("\nYou selected a mine! You lose! Here are all the positions of the mines!")

				for x in range(height):

					for y in range(width):

						if board[x][y] == '*':

							hidden[x][y] = board[x][y]




				print('  ',*horizontal)

				print('  ',*line)

				for x in range(height): # Print board

					print((str(x)+'|'),*board[x])



				quit()



			elif board[ypos][xpos] != '*' and action.lower() == 'm':

				print("\nYou landed on the number:",board[ypos][xpos])

				hidden[ypos][xpos] = board[ypos][xpos]

				if hidden[ypos][xpos] == 0:

					if ypos+1 < height:

						hidden[ypos+1][xpos] = board[ypos+1][xpos]

					if ypos-1 >= 0:

						hidden[ypos-1][xpos] = board[ypos-1][xpos]

					if ypos+1 < height and xpos+1 < width:

						hidden[ypos+1][xpos+1] = board[ypos+1][xpos+1]

					if ypos-1 >= 0 and xpos+1 < width:

						hidden[ypos-1][xpos+1] = board[ypos-1][xpos+1]

					if ypos-1 >= 0 and xpos-1 >= 0:

						hidden[ypos-1][xpos-1] = board[ypos-1][xpos-1]

					if xpos+1 < width:

						hidden[ypos][xpos+1] = board[ypos][xpos+1]

					if xpos-1 >= 0:

						hidden[ypos][xpos-1] = board[ypos][xpos-1]

					if ypos+1 < height and xpos-1 >= 0:

						hidden[ypos+1][xpos-1] = board[ypos+1][xpos-1]

					
					for x in range(height*width):  # Zero search algorithm called for each coordinate

						zero()


			elif board[ypos][xpos] == '*' and action.lower() == 'f':

				winflag = winflag + 1

				hidden[ypos][xpos] = '!'


			elif board[ypos][xpos] != '*' and action.lower() == 'f':

				hidden[ypos][xpos] = '!'

				print("\nYou have flagged a safe square! The square you have flagged is not a bomb! You lose!\n")

				print('  ',*horizontal)

				print('  ',*line)

				for x in range(height): # Print board

					print((str(x)+'|'),*board[x])

				quit()


			if winflag == bombs and hidden.count('?') == 0:

				print("\nYou win! You have explored or flagged every square and you have only flagged bombs!\n")

				quit()




	else:  # Max bomb limit

		print("\nThis number of bombs does not work with the board size. You cannot have",bombs,"bombs with",str(width*height),"square units board size! Also, you cannot have 0 bombs. You must have at least a bit of danger!")

		quit()

except ValueError: # Enter three integers into the console

	print("\nPlease enter 3 integers: A width, a height, and a number of bombs.")

	quit()












