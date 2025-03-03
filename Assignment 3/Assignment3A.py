# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: Assignment 3A

# Program Assignment3A.py

# Assignment3A: Number Diamond

# This program generates a diamond pattern of numbers using nested loops. The shape will be
# composed of single digit numbers 0-9. The size of the diamond will be determined by a single
# value inputted by the user.

# Requirements:

# Your solution must use a nested FOR loop exclusively.

# Assume the user will input any positive value for the input.

# The input size will determine the diamond's height and width.

# For this shape to work, we can only use odd values for size. If the user enters an even number, the
# program will automatically increase it by 1.

# Use the Modulus % operator to figure out if the value is even or odd.

# The diamond should be filled with increasing single digit numbers starting from 0 to 9. Once the
# number gets to 9, we will re-start from 0 and so on. Use the Modulus % operator for this.

# As always, you must follow the output format provided in the Sample Outputs

# Hints:

# You may have to heavily rely on Modulus for this lab so make sure you understand how to use them.

# Count how many numbers and how many "left side empty spaces" there are on each line and see if
# you notice a pattern. 

size = int(input("Enter an odd number for the size of the diamond: "))

if size % 2 == 0:
    print("Size must be an odd number; we will increase it to", size + 1)
    size += 1

middle = size // 2
counter = 0

for row in range(size):
    if row <= middle:
        spaces = middle - row
        numbers = 2 * row + 1
    else:
        spaces = row - middle
        numbers = 2 * (size - row) - 1
        
    for space in range(spaces):
        print(" ", end="")
    
    for num in range(numbers):
        print(counter % 10, end="")
        counter += 1

    print()  

