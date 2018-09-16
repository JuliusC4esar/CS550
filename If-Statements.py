# Kai

# Sept. 16, 2018

# If Statement practice: Prints out a grade based on number from 0-5 entered as a command line argument

import sys

number = float(sys.argv[1])

text = "You have received a "
	
if 0<=number<1.5:
	print(text + "D-")
elif 1.5<=number<2:
	print(text + "D")
elif 2<=number<2.5:
	print(text + "D+")
elif 2.5<=number<2.85:
	print(text + "C-")
elif 2.85<=number<3.2:
	print(text + "C")
elif 3.2<=number<3.5:
	print(text + "C+")
elif 3.5<=number<3.85:
	print(text + "B-")
elif 3.85<=number<4.2:
	print(text + "B")
elif 4.2<=number<4.5:
	print(text + "B+")
elif 4.5<=number<4.7:
	print(text + "A-")
elif 4.7<=number<4.85:
	print(text + "A")
elif 4.85<=number<=5:
	print(text + "A+")
else:
	print("Please enter a number (inclusive) between 0 and 5.")


	
