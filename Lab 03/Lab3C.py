# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: 3C

# Program Lab3C.py
# Design a program that determines how long an oven at a sandwich shop will take
# to heat up a sandwich.

# user inputs
small = input ("Enter the number of small sandwiches: ")
medium = input ("Enter the number of medium sandwiches: ")
large = input ("Enter the number of large sandwiches: ")
extraLarge = input ("Enter the number of extra-large sandwiches: ")

# calculations
smallTime = int (small) * 30
mediumTime = int (medium) * 60
largeTime = int (large) * 75
extraLargeTime = int (extraLarge) * 135

totalTime = smallTime + mediumTime + largeTime + extraLargeTime
totalMinutes = int (totalTime) // 60
totalSeconds = int (totalTime) % 60

# Print output
print ("\nYou've entered " + str (small) + " small sandwiches.")
print ("You've entered " + str (medium) + " medium sandwiches.")
print ("You've entered " + str (large) + " large sandwiches.")
print ("You've entered " + str (extraLarge) + " extra-large sandwiches.")

print ("\nTotal cooking time is " + str (totalMinutes) +
       " minutes and " + str (totalSeconds) + " seconds.")