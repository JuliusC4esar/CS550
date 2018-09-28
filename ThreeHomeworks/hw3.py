# Kai

# Sept. 27, 2018

# Generates a list of random integers from a range of 1-30 and removes all numbers whose digits sum to five.


import random

numbers = []

for i in range(30):

	numbers.append(random.randint(1,30))


print("Original List:",numbers)


for i in range(30):

	x = str(numbers[i])

	try:

		if int(x[0]) + int(x[1]) == 5:

			print("Removed:",x)

	except IndexError:

		if int(x) == 5:

			print("Removed: 5")







