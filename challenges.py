import sys
import random

# First challenge

if sys.argv[1] == '1':

	print("Executing first challenge...")

	while True:

		grade = input("Enter your grade here: ")

		if len(grade) == 1:

			if grade.lower() == 'a':

				print("\nGreat job!")

			elif grade.lower() == 'b':

				print("\nMeh...")

			else:

				print("\nThat's not an A or a B... which means it's bad.")

			break

		else:

			print("\nThat's not a grade. Please enter a single letter grade.")



# Second challenge

if sys.argv[1] == '2':

	print("Executing second challenge...")

	while True:

		yards = input("Enter the number of yards: ")

		try:

			if int(yards) < 17:

				yards = int(yards) * 2

				print("\nMultiplying yards by 2...")

			else:

				print("\nDid not multiply by 2.")

			print("\nards:",str(yards))

			break

		except ValueError:

			print("\nPlease enter an integer.\n")



# Third challenge:

if sys.argv[1] == '3':

	success = False

	print("\nExecuting third challenge...")

	print("\nRandomizing true or false for boolean success...")

	rand = random.randint(0,2)

	if rand == 1:

		success = True

	if success:

		print("\ncongratulations! Success = True")

	else:

		print("\nOh no! Success = False")



# Fifth challenge:

if sys.argv[1] == '5':

	while True:

		temp = input("Please enter a temperature: ")

		temptype = input("Celsius or Farenheit? (please type in a C or an F): ")

		celsius = False

		try:

			temp = float(temp)

			if temptype.lower() == 'c':

				celsius = True

			elif temptype.lower() != 'f':

				print("You didn't type in a C or an F! Assuming celsius because it is superior...")

				celsius = True

			break


		except ValueError:

			print("That's not a valid temperature!")



	if celsius:

		temp = (1.8*temp) + 32

	print("Your farenheit value:",temp)




# Seventh challenge:

if sys.argv[1] == '7':

	while True:

		pollution = input("Enter pollution value (float): ")

		cutoff = input("Enter a cutoff value (float): ")

		try:

			pollution = float(pollution)

			cutoff = float(cutoff)

			break

		except ValueError:

			print("You didn't enter two float values!")


	if pollution < cutoff:

		print("Safe!")

	else:

		print("Dangerous!")



# Ninth challenge:

if sys.argv[1] == '9':

	thing = input("Enter your input: ")

	if len(str(thing)) > 1:

		print("symbol")

	try:

		thing = int(thing)

		if len(str(thing)) == 1:

			print("digit")

			quit()

	except ValueError:

		pass

	finally:

		if str(thing).isupper():

			print("Uppercase")

		elif str(thing).islower():

			print("lowercase")




# Eleventh Challenge:

if sys.argv[1] == '11':

	while True:

		in1 = input("Does the contestant do significant work? (t/f): ")

		in2 = input("Did the contestant make a breakthrough? (t/f): ")

		doessignificantwork = False

		makesbreakthrough = False

		if (in1 == 't' or in1 == 'f') and (in2 == 't' or in2 == 'f'):

			if in1.lower() == 't':

				doessignificantwork = True

			if in2.lower() == 't':

				makesbreakthrough = True

			break

		else:

			print("Type in t or f.")

	if doessignificantwork and makesbreakthrough:

		print("Nobel Prize winner.")

	else:

		print("Not Nobel Prize winner.")



# Thirteenth Challenge:

if sys.argv[1] == '13':

	word = input("Enter your word: ")

	if word[len(word)-1].lower() == 'y' and word[len(word)-2].lower() == 'l':

		print("Adverb.")

	elif word[len(word)-1].lower() == 's':

		print("Plural.")

	elif word[len(word)-3].lower() == 'i' and word[len(word)-2].lower() == 'n' and word[len(word)-1].lower() == 'g':

		print("Gerund.")

	else:

		print("Error.")


# Fifteenth Challenge:

if sys.argv[1] == '15':

	while True:

		leapyear = False

		try:

			year = input("Enter the year: ")

			year = int(year)

			if year%4 == 0 and year%100 != 0:

				leapyear = True

			elif year%100 == 0 and year%400 == 0:

				leapyear = True

			break

		except ValueError:

			print("Please enter an integer year.")


	if leapyear:

		print("Leapyear.")

	else:

		print("Not leapyear.")



# Seventeenth Challenge:

if sys.argv[1] == '17':

	while True:

		specialnumber = False

		number = input("Enter your number: ")

		try:

			number = int(number)

			break

		except ValueError:

			print("Not a special number.")

			quit()


	if number%2 == 0 and number%5 == 0 and number >= -100 and number <= 100:

		specialnumber = True

		print("Special Number!")

	else:

		print("Not special number.")



# Nineteenth Challenge:

if sys.argv[1] == '19':

	dayOfWeek = input("Enter the abbreviated day of the week (mon, tue, wed, thu, fri, sat, sun): ")

	isweekend = False

	if dayOfWeek.lower() == 'sat' or dayOfWeek.lower() == 'sun':

		isweekend = True

		print("Weekend! Woohoo!")

	elif dayOfWeek.lower() == 'mon' or dayOfWeek.lower() == 'tue' or dayOfWeek.lower() == 'wed' or dayOfWeek.lower() == 'thu' or dayOfWeek.lower() == 'fri':

		print("Not weekend.")

	else:

		print("I don't recognize that day!")


# Twenty-First Challenge:

if sys.argv[1] == '21':

	while True:

		validtriangle = False

		ang1 = input("Enter first angle: ")

		ang2 = input("Enter second angle: ")

		ang3 = input("Enter third angle: ")

		try:

			ang1 = int(ang1)

			ang2 = int(ang2)

			ang3 = int(ang3)

			break

		except ValueError:

			print("Please enter three integer values.")


	if (ang1 + ang2 + ang3) == 180:

		print("Valid triangle!")

		validtriangle = True

	else:

		print("Not valid triangle!")



# Twenty-Third Challenge:

if sys.argv[1] == '23':

	greeting = None

	language = None

	language = input("Enter your language: ")

	if language.lower() == "english":

		greeting = "Hello."

	elif language.lower() == "french":

		greeting = "Bonjour."

	elif language.lower() == "spanish":

		greeting = "Hola."

	else:

		greeting = "I do not recognize that language."

	print(greeting)



# Twenty-Fifth Challenge:

if sys.argv[1] == '25':

	userinput = input("Enter your input: ")

	if userinput.lower() == "bacon":

		print("Why did you type bacon?")

	else:

		print("I like bacon.")





#4
word = input("enter a word")

letter = word[1]

if letter == "f":
  print("fun")

else:
  print("no")

#6 
#Variable numItems is an int. Variable averageCost and totalCost are floats. If there are items, calculate the average cost. If there are no items, print no items.

numItems = 10
totalcost = 399.50

if numItems:
	averageCost = totalcost/numItems
	print(averageCost)

else:
	print("no items!")


#8
 #Variable score is a float, and grade is a char. Store the appropriate letter grade in the grade variable according to this chart.
 #F: <60; B: 80-89; D: 60-69; A: 90-100; C: 70-79.
 
score = 76
grade = None 
if score < 60:
	grade = F
   
elif score >= 60 and score <= 69:
  grade = D
  
elif score > 69 and score <=79:
  grade = C
  
elif score > 79 and score <=89:
  grade = B
  
elif score > 89:
  grade = A
  
  
#10. 
#Variable neighbors is an int. Determine where you live based on your neighbors.
#50+: city; 25+: suburbia; 1+: rural; 0: middle of nowhere. 


neighbors = input("How many neighbors do you have?")

if neighbors >= 50:
  print("you live in the city")

elif neighbors < 50 and neighbors >= 25:
  print("you live in suburbia")
  
elif neighbors <25 and neighbros >=1:
  print("you live in a rural area")
  
elif neighbors == 0:
  print("middle of nowhere")
  
#12. 
#Variable tax is a boolean, price and taxRate are floats. If there is tax, update price to
#reflect the tax you must pay.

tax = true

price = 300

taxrate = 0.25

if tax:
  price = price + (taxrate*price)
  print(price)
  
#14. 
# If integer variable currentNumber is odd, change its value so that it is now 3 times currentNumber plus 1, otherwise change its value so that it is now half of currentNumber (rounded down when currentNumber is odd). 

currentNumber = 13

if currentNumber%2 == 0:
  currentNumber = currentNumber/2
else:
  currentNumber = (3*currentNumber) + 1
  
#16. 
#Determine the smallest of three ints, a, b and c. Store the smallest one of the three in int result. 

a = 10
b = 13
c = 12

list = [a,b,c]
result = list[0]
for x in list:
  if x<result:
    result = x
  return result
  
#18. 
#Variable letter is a char. Determine if the character is a vowel or not by storing a letter code in the int variable code.
#a/e/o/u/i: 1; y: -1; everything else: 0


letter = a
code = 1

if code == 1:
  print("your character is a vowel")
elif code == -1 or code == 0:
  print("your character isn't a vowel")
  
#20 
#Given a String variable month, store the number of days in the given month in integer variable numDays. 

month = input("enter your month name")

if lower(month) == "january" or lower(month) == "march" or lower(month) == "may" or lower(month) == "july" or lower(month) == "august" or lower(month) == "october" or lower(month) == "december" :
  numDays = 31
  print(numDays)
  
elif lower(month) == "april" or lower(month) == "june" or lower(month) == "september" or lower(month) == "november":
  numDays = 30
  print(numDays)
  
else:
  numDays = 28
  print(numDays)
  
#22
#Given an integer, electricity, determine someone's monthly electric bill, float payment, following the rubric below. 

electricity = int(input("how much electricity?")

if electricity >= 50 and electricity <= 150:
	payment = (50*0.5) + (electricity-50)*(75)
  
if electricity > 150 and electricty <= 250:
	payment = (50*0.5) + (100)*(0.75) + (electricity-150)*(1.2)
  
if electricity > 250:
	payment = electricity*1.5 + (electricity*0.2)
  
# 24. 
#Generate a phrase and store it in String phrase, given an int number and a String noun. Here are some sample phrases:
#number: 5; noun: dog; phrase: 5 dogs
#number: 1; noun: cat; phrase: 1 cat
#number: 0; noun: elephant; phrase: 0 elephants
#number: 3; noun: human; phrase: 3 humans
#number: 1; noun: home; phrase: 3 homes

number = input("number")
noun = input("noun")

if number == 1:
  print(number+noun)
  
else:
  print(number+noun+"s")
  
  
#26.
#Come up with your own creative tasks someone could complete to practice if-statements. Also provide solutions.


#if an input number is even, multiply it by 3 if it is less than 10 and multiply it by 15 if it is greater than or equal to ten. If it is odd, keep doubling it until it is greater than or equal to 100.

#SOLUTION

number = int(input("number")

if number%2 == 0:
  if number<10:
    number = number*3
  else:
    number = number*15

else:
	while number < 100:
    	number = number*2





		