# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: Lab 7A

# Program Lab7A.py

# Lab7A: Rectangle Area and Perimeter Calculator

# This program will calculate the area and perimeter of a rectangle by asking the user for the width
# and height value of the rectangle. The program should validate the rectangle input by checking if the
# sum of the width and height is greater than 30.

# Requirements:

# For this program, you must implement and use the specified methods, or it will not be graded.

# Design and implement a program that implements the following methods:

    # Method isValid() which takes in two values: width and height, and returns True if the
    # sum of width and height is greater than 30, otherwise, return False.
        # isValid(width, height):

    # Method area() which takes in two values: width and height, and calculates and returns
    # the area of the rectangle.
        # area(width, height):

    # Method perimeter() which takes in two values: width and height, and calculates and
    # returns the perimeter of the rectangle.
        # perimeter(width, height):

# The user should be able to input fractional values for width and height.

# Before calculating and outputting the area and perimeter, the program should check if the width and
# height values form a valid rectangle.

# Print "This is an invalid rectangle." if the width and height do not form a valid rectangle. Otherwise
# output the area and perimeter.

# Allow the user to re-run the program.

# Before termination, output "Program Ends"

# Hints:
# Remember that we specifically used the word return for the specification for each function.
# Remember to use the isValid() function to validate the width and height of the rectangle.
# We only calculate the area and perimeter if the rectangle is valid.

def isValid(width, height):
    return width + height > 30

def area(width, height):
    return width * height

def perimeter(width, height):
    return 2 * (width + height)

while True:
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    
    if isValid(width, height):
        print("This is a valid rectangle.")
        print("The area is:", area(width, height))
        print("The perimeter is:", perimeter(width, height))
    else:
        print("This is an invalid rectangle.")
    
    print("\nDo you want to enter another width and height (Y/N)?: ", end="")
    choice = input().upper()
    print()
    
    if choice != 'Y':
        print("Program Ends")
        break


