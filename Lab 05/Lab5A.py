# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: 5A

# Program Lab5A.py
# # For this lab, you will write a program that will ask the user to input 10 positive integer numbers, one
# # at a time. While it does this, the program should also keep track of the largest number the user has
# # entered so far. Once the user enters 10 positive integers, the program should display the largest
# # number entered by the user.

print("Please enter 10 numbers and this program will display the largest.")

num1 = 0
largest = 0

for num in range(1,11):
     num1 = int(input("Please enter number " + str(num) + ": "))
     if num1 > largest:
         largest = num1

print("The largest number was " + str(largest))

