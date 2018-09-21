

try:

	num = int(input("Pick a number between 1 and 5\n"))

	while num > 5 or num < 1:

		print("I said, pick a number between 1 and 5.")

		num = int(input("Pick a number between 1 and 5\n"))

		if ValueError:

			print("That's not an integer")


print("Success")