# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: 3A

# Program Lab3A.py
# Write a program that prompts the user for their Current.
# Balance on their credit card and their
# Annual.Percentage.Rate.(APR) of the card.

currentBalance = float(input ("Amount owed: $"))
APR = float(input ("APR: "))
MPR =  (APR / 100) / 12
minimumPayment = float(currentBalance) * float(MPR)
print ("Monthly percentage rate: " +  str(round(MPR * 100, 3)))
print("Minimum payment: $" +  str(round(minimumPayment, 2)))