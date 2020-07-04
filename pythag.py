while 1:
	menu = "What would you like:\n 1. Find a hyptenuse \n 2. Find another side \n 9. Exit\n Enter an option."

	x = int(input(menu))
	if x == 1: 
		y = int(input("Enter the length of the one of the known sides ")) 
		z = int(input("Enter the length of the other known side "))
		hyp =  ((y**2 + z**2)**0.5)
		print("The length of the missing side is " + str(hyp))
    
#	elif x == 2: 
#		a = int(input("Enter the length of the hypotenuse ")) 
#		b = int(input("Enter the length of the other known side "))
#		side = (a**2 - b**2)**0.5
#		print("The length of the missing side is " + str(side))   

	elif x == 9:
		print("Good bye!")
		break

	else:
		print("Not a valid input. Try again.")
