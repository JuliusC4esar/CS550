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

			print("You can't withdraw that much money! Your balance:",balance)

		else:

			self.balance = int(self.balance) - intake

			print(intake,"dollars withdrawn. Your balance is now",self.balance)



account = Account(500,23,12345)


password = input("Enter your PIN: ")

if password == str(account.pin):

	print("\nAccount Unlocked. Welcome, customer!\n")

	while True:

		action = input("Action: ")

		if action.lower() == "withdraw":

			account.withdraw()


else:

	print("Wrong PIN")

	quit()
