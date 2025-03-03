# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: 5B

# Program Lab5B.py
# For this lab we will write a program that will print a box, and
# right triangles made of asterisks `*`.
# The size of each shape will be based on a size input by the user.

size = int(input("Please enter a value for the size: "))

# Box
print("This is the requested " + str(size) + "x" + str(size) + " box:")
for row in range(size):
    for column in range(size):
        print("*", end="")
    print()

# Right Facing Triangle
print("This is the requested right-facing " + str(size) + "x" + str(size) + " right-triangle:")
for row in range(size + 1):
    for column in range(row):
        print("*", end="")
    print()

# Left Facing Triangle
print("This is the requested left-facing " + str(size) + "x" + str(size) + " right-triangle:")
for row in range(size + 1):
    for column in range(size - row):
        print(" ", end="")
    for column in range(row):
        print("*", end="")
    print()