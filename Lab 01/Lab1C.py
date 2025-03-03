# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: 1C

# Program Lab1C.py
# Demonstrate the use of the input function to read numeric data.
# Calculates fuel efficiency based on values entered by the user.
miles = float(input ("Enter the number of miles: "))
gallons = float(input ("Enter the gallons of fuel used: "))
mpg = miles / gallons
print ("Miles Per Gallon: " + str (mpg))