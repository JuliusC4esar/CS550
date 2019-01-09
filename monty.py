# Kai
# Monty Hall Problem
# Switching makes a monumental difference in your chances of winning the car. This is because when you make the original choice of three random boxes, you have a 2/3 chance of getting pennies. After one penny box is revealed, if you have selected a penny box, you are guaranteed to get the car if you switch. Therefore, by switching, you have a 2/3 chance of winning the car. However, by not switching, you have a mere 1/3 chance of winning the car by virtually nullifying the effect of revealing a penny box.

import random

car = 0

pennies = 0

for x in range(1000):

	r = random.randint(1,3) # Random choice between three options. Let 1 and 2 represent pennies, and 3 represent the car.

	if r != 3: # If 1 or 2 is selected, get pennies.

		pennies = pennies + 1

	else:

		car = car + 1


print("")

print("IF YOU DO NOT SWITCH:")

print("Times car is won: " + str(car))

print("Times pennies are won: " + str(pennies),"\n")	


car = 0

pennies = 0

for x in range(1000):

	r = random.randint(1,3) # Random choice between three options.

	if r == 3: # By selecting the car, if you switch you will get pennies.

		pennies = pennies + 1

	else: # By selecting pennies, if you switch after the reveal you will get a car.

		car = car + 1

print("IF YOU SWITCH:")

print("Times car is won: " + str(car))

print("Times pennies are won: " + str(pennies),"\n")	


# The results are as I predicted. On average, you have a 2/3 chance of winning the car if you switch and a 1/3 chance if you do not switch. My explanation for the logic of the problem is at the top of the script.






