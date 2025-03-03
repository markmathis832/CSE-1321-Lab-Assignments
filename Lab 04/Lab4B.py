# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: 4B

# Program Lab4B.py
# create a basic program which will allow the user to
# select an option from a menu; selecting a different
# option from the menu should result in a different outcome.

# User input
print ("Welcome!")
number = float(input("Please input a number: "))

print("What would you like to do with this number: ")
print("0) Get the additive inverse of the number")
print("1) Get the reciprocal of the number")
print("2) Square the number")
print("3) Cube the number")
print("4) Exit the program")

choice = int(input())

# Match statements
match choice:
    case 0:
       inverse = number / -1
       print("The additive inverse of " + str(number) + " is " + str(inverse))
    case 1:
        if number == 0 or number == 0.0:
            print("Cannot divide by 0!")
        else:
            reciprocal = 1 / number
            print("The reciprocal of " + str(number) + " is " + str(round(reciprocal, 3)))
    case 2:
        square = number * number
        print("The square of " + str(number) + " is " + str(square))
    case 3:
        cube = number * number * number
        print("The cube of " + str(number) + " is " + str(cube))
    case 4:
        print("Thank you, goodbye!")
    case _:
        print("Invalid option!")