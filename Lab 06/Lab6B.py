# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: 6B

# Program 6B.py

import random

random_number = random.randint(1, 100)

print("Guess the number I am thinking!")
user_guess = int(input("Enter any number between 1 and 100:"))

while user_guess != random_number:
    if user_guess < random_number:
        print("Too low!")
    elif user_guess > random_number:
        print("Too high!")
    user_guess = int(input("Enter any number between 1 and 100:"))


print("Correct! I was thinking of " + str(random_number))

