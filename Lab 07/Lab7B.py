# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: Lab 7B

# Program Lab7B.py

# Lab7B: Max and Min of two numbers

# This simple program will ask the user for two numbers, then the program should output which
# number is the lowest of the two, which number is the largest of the two, and the average of both
# numbers.

# Requirements:
# For this program, you must implement and use the specified methods, or it will not be graded.
# Implement two python files, one called MyMath which will contain the methods and Lab7B which
# will have the main logic and implementation of the program.

# Inside of MyMath.py, write the following methods:
# my_max which takes in two number values and returns the largest between the two inputs.
# my_min which takes in two number values and returns the smallest between the two inputs.
# my_avg which takes in two number values and returns the calculated mean average of the two inputs.

# In Lab7B:

# The program your prompt and read two number values.
# These values should be taken in as an integer.
# Import and call the methods implemented in MyMath.py.
# Call the appropriate methods and output the corresponding values.

# Hint:
# Remember that we specifically used the word return for the specification for each function

from MyMath import my_min, my_max, my_avg

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print("Min is ", my_min(num1, num2))
print("Max is ", my_max(num1, num2))
print("Average is ", my_avg(num1, num2))


