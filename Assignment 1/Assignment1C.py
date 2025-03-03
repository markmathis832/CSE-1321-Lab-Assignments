# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: Assignment 1C

#Centimeters to Feet and Inches Converter

print ("[Centimeters to Feet and Inches Converter]")

# user input
centimeters = input ("Enter the lenth in centimeters: ")

# Calculations
feet = float (centimeters) // 30.48
feetRemainder = float (centimeters) % 30.48
inches = float (feetRemainder) / 2.54

# Output
print ("The length is " +  str (int (feet)) + " feet and " + str (round(inches, 2)) + " inches")