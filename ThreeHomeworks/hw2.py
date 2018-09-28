# Kai

# Sept. 27, 2018

# Generates a random list of six multiples of 13 and then removes all numbers with the digit 6


import random

numbers = []

for i in range(6):

	numbers.append(13*random.randint(1,20))


print("Original List:",numbers)


for i in range(6):

	x = str(numbers[i])

	for y in range(len(x)):

		if x[y] == '6':

			print("Removed:",x)

			

