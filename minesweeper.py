# Kai
# October 2, 2018
# Functional minesweeper board generation
# Enter 3 integers: a width, a height, and a number of bombs, and a minesweeper board will be generated.





# Board generation starts here:

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







	# Input starts here:


	while True:

			while True:

				try:

					xpos = int(input("\nEnter the x-coordinate of the item you wish to select. (The bottom left corner has coordinates (1,1), so coordinates start at 1 and go up with the array.)\n"))

					ypos = int(input("\nEnter the y-coordinate of the item you wish to select. (The bottom left corner has coordinates (1,1), so coordinates start at 1 and go up with the array.)\n"))

					if xpos >= 1 and xpos <= width and ypos >= 1 and ypos <= height:

						break

					else:

						print("\nPlease enter an integer that is greater than or equal to one and is within the parameters of the array.\n")

				except ValueError:

					print("\nPlease enter an integer that is greater than or equal to one and is within the parameters of the array.\n")




			if board[(height-(ypos-1))-1][xpos-1] == '*':

				print("\nYou selected a mine! You lose!")

				quit()

			else:

				print("\nYou selected the number:",board[(height-(ypos-1))-1][xpos-1])


			for x in range(height):

				print(*board[x])






except ValueError:

	print("Please enter 3 integers: A width, a height, and a number of bombs.")

	quit()



