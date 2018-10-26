class Account:

	def __init__(self,balance,number,pin):

		self.balance = balance

		self.number = number

		self.pin = pin


	def withdraw(self):

		while True:

			intake = input("\nHow much money would you like to withdraw?\n")

			try:

				intake = int(intake)

				break

			except ValueError:

				print("That's not a number. (do not include spaces or letters or special characters. only include integers.)")


		if intake > int(self.balance):

			print("You can't withdraw that much money! Your balance:",self.balance)

		else:

			self.balance = int(self.balance) - intake

			print(intake,"dollars withdrawn. Your balance is now",self.balance)


	def deposit(self):

		while True:

			intake = input("\nHow much money would you like to deposit?\n")

			try:

				intake = int(intake)

				break

			except ValueError:

				print("That's not a number. (do not include spaces or letters or special characters. only include integers.)")


		self.balance = int(self.balance) + intake

		print(intake,"dollars deposited. Your balance is now",str(self.balance))


	def num(self):

		print("Your account number is:",self.number)



account = Account(500,23,12345)


password = input("Enter your PIN: ")

if password == str(account.pin):

	print("\nAccount Unlocked. Welcome, customer!\n")

	while True:

		action = input("Action (withdraw/deposit/number/exit): ")

		if action.lower() == "withdraw":

			account.withdraw()

		elif action.lower() == "deposit":

			account.deposit()

		elif action.lower() == "number":

			account.num()

		elif action.lower() == "exit":

			print("Thank you for using this ATM! Goodbye.")

			quit()


else:

	print("Wrong PIN")

	quit()
