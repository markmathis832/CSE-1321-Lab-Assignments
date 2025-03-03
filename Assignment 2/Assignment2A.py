# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: Assignment 2A

# Program Assignment2A.py
# Write a Python program to calculate the discount on an
# online shopping order based on the customer's
# total purchase amount and their membership status.

print("[Discount Calculator]")

#User Input
purchase = float(input("Enter your total purchase amount: $"))
member = (input("Are you a member of the shopping club (Yes or No)?"))

#Input Validation / Statements
if member in ["Yes","YES","yes"] or member in ["No","NO","no"]:

    if purchase > 200.00:

        if member in ["Yes","YES","yes"]:
            discount = purchase * .15
        else:
            discount = purchase * .10

    elif purchase > 50.00 and purchase <= 200.00:

        if member in ["Yes","YES","yes"]:
            discount = purchase * .10
        else:
            discount = purchase * .05

    else:
        discount = 0.00

else:
    print("Please enter Yes/YES/yes or No/NO/no.")

total = purchase - discount

# Output
print("Your discount is: $" + str(round(discount, 1)))
print("Your total price after discount is: $" + str(round(total, 1)))