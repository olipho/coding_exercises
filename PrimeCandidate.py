""" 
Filename: 
Author: 
Date: 
Description: 
"""
while True:
    x = int(input("Welcome to Prime Candidacy. \n Enter your lower bound for your prime number search."))

    y = int(input("Enter your upper bound for your prime number search."))

    z = y - x
    print(z)
    if z < 201:
        primes = []
        sqrt = y**0.5
        print("All good")
            if z < 0 
            swap  = x
            x = y
            y = swap
            print("Your values have been swapped as your upper bound needs to be higher than your lower bound. x = " + str(x) + " and y = " + str(y))
    elif z >= 201:
        high = x + 200
        low = y - 200
        print("The difference in your selection of numbers is too large. Please choose two values with a difference of 200 or less.")
        x = int(input("Enter your lower bound for your prime number search."))
        y = int(input("Enter your upper bound for your prime number search."))

    elif z == 0:
        print("You've entered the same values. Please re-enter.")

    else:
        print("What else can go wrong?")
