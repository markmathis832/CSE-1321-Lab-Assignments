# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: Assignment2B

# Program Assignment2B.py
# Based on the inputs, determine whether the user qualifies for a loan and what type of loan they
# qualify for. Use nested if-elif-else statements and the program must use a match statement to
# classify the person's credit score into categories.

# User Input
print("[Loan Approval System]")
age = int(input("Enter your age: "))
income = int(input("Enter your income: "))
numScore = int(input("Enter your credit score: "))

# Age validation
if age >= 18:

    if numScore >= 300 and numScore <= 850:

        match numScore:
            case numScore if numScore >= 700 and numScore <= 850:
                score = "Good"
            case numScore if numScore >= 600 and numScore <= 699:
                score = "Fair"
            case numScore if numScore >= 300 and numScore <= 599:
                score = "Poor"

        if score == "Good" or score == "Fair":

                if income >= 100000 and score == "Good":

                    print("You qualify for a Premium Loan")

                elif (income >= 50000 and income < 100000) and (score == "Good" or score == "Fair"):

                    print("You qualify for a Standard Loan")

                elif income < 50000 and score == "Fair":

                    print("You qualify for a Basic Loan")

                else:
                    print("Your income is too low for a loan.")

        else:
            print("You do not qualify for a loan due to poor credit.")

    else:
        print("Credit score must be between 300 and 850")

else:
    print("You do not qualify for a loan due to age.")