# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: Assignment 1B

#  Calculate the pressure of gas using
# the Ideal Gas Law equation

print ("[Ideal Gas Law Calculator]")

# User input
moles = input ("Enter the number of moles of the gas: ")
TCelcius = input ("Enter the temerature of the gas in Celcius: ")
volume = input ("Enter the volume of the gas in Liters: ")

# Calculations
R = 0.0821
TKelvin = float (TCelcius) + 273.15
nRT = (float (moles)) * (float (R)) * (float (TKelvin))
P = (float (nRT)) / (float (volume))

# Output
print ("The pressure of the gas is " + str (float (round(P, 2))) + " atm")