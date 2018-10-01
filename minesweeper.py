# Kai
# Minesweeper Board
# Enter three console values: width, height, and number of bombs. A board will be generated with bombs randomly positioned.
# While I successfuly completed the random bomb generation as well as the board dimensional generation, I could not complete the final step. The code that I wrote for the number generation is still written, but I cannot figure out what is incorrect.


import random

import sys

import math

width = int(sys.argv[1])

height = int(sys.argv[2])

bombs = int(sys.argv[3])

board = [[0] for x in range(height)]

for x in range(height):

	for i in range(width-1):

		board[x].append(0)


for x in range(bombs):

	board[random.randint(0,height-1)][random.randint(0,width-1)] = '*'


for x in range(height):

	for i in range(width):

		try:

			if board[x][i + 1] == '*':

				board[x][i] = (board[x][i])+1

		except:

			break

		try:

			if board[x + 1][i + 1] == '*':

				board[x][i] = (board[x][i])+1

		except:

			break

		try:

			if board[x][i - 1] == '*':

				board[x][i] = (board[x][i])+1


		except:

			break

		try:

			if board[x - 1][i - 1] == '*':

				board[x][i] = (board[x][i])+1

		except:

			break

		try:

			if board[x - 1][i - 1] == '*':

				board[x][i] = (board[x][i])+1

		except:

			break


		try:

			if board[x - 1][i + 1] == '*':

				board[x][i] = (board[x][i])+1

		except:

			break

		try:

			if board[x + 1][i - 1] == '*':

				board[x][i] = (board[x][i])+1

		except:

			break


		try:

			if board[x + 1][i] == '*':

				board[x][i] = (board[x][i])+1

		except:

			break


		try:

			if board[x - 1][width] == '*':

				board[x][i] = (board[x][i])+1

		except:

			break





for x in range(height):

	print(board[x])







