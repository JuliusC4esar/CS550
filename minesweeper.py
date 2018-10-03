# Kai
# October 2, 2018
# Functional minesweeper board generation
# Enter 3 integers: a width, a height, and a number of bombs, and a minesweeper board will be generated.


import random

import sys

try:

	width = int(sys.argv[1])

	height = int(sys.argv[2])

	bombs = int(sys.argv[3])

	board = [[0] for x in range(height)]

	
	for x in range(height):

		for y in range(width-1):

			board[x].append(0)



	for x in range(height):

		print(*board[x])


	for b in range(bombs):

		x = random.randint(0,height-1)

		y = random.randint(0,width-1)

		if board[x][y] != '*':

			board[x][y] = '*'

		else:

			b = b-1


		if board[x][y] == '*':

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


	print()

	for x in range(height):

		print(*board[x])


except ValueError:

	print("Please enter 3 integers: A width, a height, and a number of bombs.")

	quit()



