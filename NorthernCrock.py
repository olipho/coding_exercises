### Need to remember how to use loops to return to main menu and to handle bad inputs

balance = 67.14

while 1:
	menu = "Welcome to Northern Crock. \n 1. Display balance \n 2. Withdraw funds \n 3. Deposit funds \n 9. Return Card \n Enter an option."

	x = int(input(menu))


######### Display balance ##########
	if x == 1: 
		print(round(balance,2))
			
######## Withdraw Funds ###########   
	elif x == 2: 
		menu2 = "How much would you like to withdraw? \n 1. 10 \n 2. 20 \n 3. 40 \n 4. 60 \n 5. 80 \n 6. 100 \n 7. Other Amount \n 8. Return to Main Menu  \n 9. Return Card \n Enter an option." 

		y = int(input(menu2))
	
		if y == 1:
			if balance >= 10:
				balance -= 10
				print("Please take your cash. Your new balance is " + str(round(balance,2)))
			else:
				print("You do not have sufficient funds for this transaction.")

		elif y == 2:
			if balance >= 20:
				balance -= 20
				print("Please take your cash. Your new balance is " + str(round(balance,2)))
			else:
				print("You do not have sufficient funds for this transaction.")

		elif y == 3:
			if balance >= 40:
				balance -= 40
				print("Please take your cash. Your new balance is " + str(round(balance,2)))
			else:
				print("You do not have sufficient funds for this transaction.")

		elif y == 4:
			if balance >= 60:
				balance -= 60
				print("Please take your cash. Your new balance is " + str(round(balance,2)))
			else:
				print("You do not have sufficient funds for this transaction.")

		elif y == 5:
			if balance >= 80:
				balance -= 80
				print("Please take your cash. Your new balance is " + str(round(balance,2)))
			else:
				print("You do not have sufficient funds for this transaction.")

		elif y == 6:
			if balance >= 100:
				balance -= 100
				print("Please take your cash. Your new balance is " + str(round(balance,2)))
			else:
				print("You do not have sufficient funds for this transaction.")

		elif y == 7:
			take = int(input("How much would you like to withdraw?"))
			if take % 10 == 0:
				balance = balance - take
				print("Your request has been processed. Your new balance is " + str(balance))
			else:
				print("Sorry, that amount is not supported by this ATM. Please try again.")

		elif y == 8:
			print("Returning to main menu.")

		elif y == 9:
			print("Thank you for visiting Northen Crock!")
			break

		else:
			print("Not a valid input. Try again.")


#######Deposit Funds####################
	elif x == 3:
		deposit = float(input("How much would you like to deposit?"))
		if deposit % 1 == 0: 		# work around. can't get this to function at all without the 'if' statement. 
			balance = balance + deposit
			print("Your request has been processed. Your new balance is " + str(balance))
		else:
			balance = balance + deposit
			print("Your request has been processed. Your new balance is " + str(balance))
###########################

	elif x == 9:
		print("Thank you for visiting Northen Crock!")
		break

	else:
		print("Not a valid input. Try again.")