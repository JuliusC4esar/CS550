# Kai

# Sept. 27, 2018

# Generates a list of 10 numbers from a range of 1-100. Orders list from largest to smallest. Removes all numbers divisible by 3.

# Sources: https://www.youtube.com/watch?v=D3JvDWO-BY4

import random

numbers = []

for i in range(10):

	x = random.randint(1,100)

	numbers.append(x)


print("Original List:",numbers)

numbers.sort()

secondnumbers = sorted(numbers, reverse = True)

print("Ordered List:",secondnumbers)


for i in range(10):

	if secondnumbers[i]%3 == 0:

		print("Removed:",secondnumbers[i])


