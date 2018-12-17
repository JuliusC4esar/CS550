# Kai Joseph
# Loop Practice
# Since I worked on my own, I did not have to complete all 25 challenges (with Ms. Healey's permission). I completed a total of 14 challenges.


import sys
import random


''' 1. 
   Write a for loop that will print out all the integers from 0-4 in ascending order. 
'''

if sys.argv[1] == '1':

	for x in range(5):

		print(str(x))


''' 2. 
   Write a for loop that will print out all the integers from 0-4 in descending order.
'''

if sys.argv[1] == '2':

	for x in range(5):

		print(str(4-x))



''' 3. 
   Write a for loop that will print out all the integers from 5-15 in descending order.
'''

if sys.argv[1] == '3':

	for x in range(11):

		print(str(15-x))



''' 4. 
   Write a for loop that will print out all the integers from -5 to 5 in ascending order.
'''

if sys.argv[1] == '4':

	for x in range(11):

		print(str(-5+x))




''' 5. 
   Write two for loops that will both print out odd numbers from 25 to 49. The loops themselves must be different, but they will have the same output.
'''

if sys.argv[1] == '5':

	for x in range(25,50):

		if x%2 != 0:

			print(x)

	for x in range(26):

		if x%2 == 0:

			print(str(25+x))



''' 6. 
   Write a for loop that prints out the squares of the numbers from 1 to 10. ie 1, 4, 9, 16, ... 100
'''

if sys.argv[1] == '6':

	for x in range(1,11):

		print(str(x**2))



''' 8. 
   A number starts at 4 and increases by one every day after the day it was created. Write a loop and use the variable days (int) that will print out how many days it will take for number to reach 57. 
'''

if sys.argv[1] == '8':

	for x in range(4,58):

		print(x)

		days = 57-x

		print("Days remaining to reach 57:",str(days))



''' 9. 
   A girl in your class has jellybeans in a jar. The number of jellybeans is stored in int beans. Every day she shares one jellybean with every student in the class, and she herself takes two. The number of students in the class is held in variable students (int). Write a loop that determines how many days it will take for her to run out of jellybeans. You can store the result in variable numDays (int).
'''

if sys.argv[1] == '9':

	while True:

		students = input("Number of students (excluding the girl): ")

		jellybeans = input("Number of jelly beans: ")

		try:

			students = int(students)

			jellybeans = int(jellybeans)

			break

		except ValueError:

			print("Please enter an integer for jelly beans and students.")

	days = 0

	while jellybeans > 0:

		jellybeans = jellybeans - students - 2

		days = days + 1


	print(days)





''' 17. 
   Write a loop that will print out the decimal equivalents of 1/2, 1/3, 1/4, 1/5, 1/6, ... 1/20. The output for each iteration should look like:
   "1/2 = .5" "1/3 = .666666666667" etc.
'''


if sys.argv[1] == '17':

	for x in range(2,21):

		num = 1/x

		print("1/"+str(x),"=",str(num))




''' 18. 
   Write a loop that determines the sum of all the numbers from 1-100, as well as the average. Store the sum in variable total (int) and the average in variable avg (float).
'''

if sys.argv[1] == '18':

	total = 0

	for x in range(1,101):

		total = total+x

	print("Total: "+str(total))

	avg = total/x

	print("Average: " + str(avg))




''' 19. 
   A friend tells you that PI can be computed with the following equation:
   PI = 4 * (1-1/3+1/5-1/7+1/9-1/11+1/13-1/15...)
   Write a loop that will calculate this output for n-iterations of the pattern (n being an int), that could help you determine if your friend is right or wrong. Are they right or wrong?
'''

if sys.argv[1] == '19':

	it = int(input("Enter the number of iterations: "))

	num = 0

	for x in range(1,it*2):

		if x%2 != 0:

			if (x-3)%4 == 0:

				num = num - (1/x)

			else:

				num = num + (1/x)


	print(str(4*num))



''' 22. 
   Write a loop which prints the numbers 1 to 110, 11 numbers per line. The program shall print "Coza" in place of the numbers which are multiples of 3, "Loza" for multiples of 5, "Woza" for multiples of 7, "CozaLoza" for multiples of 3 and 5, and so on. Sample output:
   1 2 Coza 4 Loza Coza Woza 8 Coza Loza 11 
   Coza 13 Woza CozaLoza 16 17 Coza 19 Loza CozaWoza 22 
   23 Coza Loza 26 Coza Woza 29 CozaLoza 31 32 Coza
   ......
'''

if sys.argv[1] == '22':

	numbers = []

	for x in range(10):

		numbers.append([])

	for x in range(1,111):

		if x < 12:

			numbers[0].append(x)

		elif x < 23:

			numbers[1].append(x)

		elif x < 34:

			numbers[2].append(x)

		elif x < 45:

			numbers[3].append(x)

		elif x < 56:

			numbers[4].append(x)

		elif x < 67:

			numbers[5].append(x)

		elif x < 78:

			numbers[6].append(x)

		elif x < 89:

			numbers[7].append(x)

		elif x < 100:

			numbers[8].append(x)

		elif x < 111:

			numbers[9].append(x)


	for x in range(len(numbers)):

		for y in range(11):

			word = ""

			tampered = False

			if int(numbers[x][y])%3 == 0:

				word = word + "Coza"

				tampered = True

			if int(numbers[x][y])%5 == 0:

				word = word + "Loza"

				tampered = True

			if int(numbers[x][y])%7 == 0:

				word = word + "Woza"

				tampered = True

			if tampered:

				numbers[x][y] = word

	for x in range(len(numbers)):

		print(*numbers[x])



''' 23.
   Write code that will print out a times-table for practice and reference. It should look like this:
    * |  1  2  3  4  5  6  7  8  9
    -------------------------------
    1 |  1  2  3  4  5  6  7  8  9
    2 |  2  4  6  8 10 12 14 16 18
    3 |  3  6  9 12 15 18 21 24 27
    4 |  4  8 12 16 20 24 28 32 36
    5 |  5 10 15 20 25 30 35 40 45
    6 |  6 12 18 24 30 36 42 48 54
    7 |  7 14 21 28 35 42 49 56 63
    8 |  8 16 24 32 40 48 56 64 72
    9 |  9 18 27 36 45 54 63 72 81
'''


if sys.argv[1] == '23':

	x = [1,2,3,4,5,6,7,8,9]

	y = x

	numbers = []

	for r in range(len(x)):

		for z in range(len(y)):

			print((int(x[r])*int(y[z])),end="  ")

		print("")



''' 25. 
   Write code that will extract each digit from an int stored in variable number, in the reverse order. For example, if the int is 15423, the output shall be "3 2 4 5 1", with a space separating the digits. 
'''

if sys.argv[1] == '25':

	number = input("Enter the number that you wish to reverse: ")

	number = str(number)

	n = []

	for x in range(len(number)):

		n.append(number[len(number)-1-x])

	for x in range(len(n)):

		print(n[x],end=" ")

	print("")



































