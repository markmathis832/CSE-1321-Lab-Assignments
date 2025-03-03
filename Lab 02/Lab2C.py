# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: 2C

# Program Lab2C.py
# create a program that will read in a width and height from the user
# and calculates the area and perimeter of a rectangle.
# The formula for perimeter is P = 2*(height+width)
# and the formula for area is A = (height*width).

width = input ("Enter a width: ")
height = input ("Enter a height: ")
area = int (height) * int (width)
perimeter = 2*(int (height) + int (width))
print("The area is " + str (area) + "\nThe perimeter is " + str (perimeter))