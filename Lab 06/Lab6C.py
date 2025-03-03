# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: 6C

# Program 6C.py

numRows = 1

while numRows != 0:
    numRows = int(input("Enter Number for Rows or 0 to quit: "))

    # Pyramid Printing
    for row in range(1, numRows + 1):
        # Print leading spaces for centering
        for column in range(numRows - row):
            print(" ", end="")

        # Print left side numbers decreasing
        for column in range(row, 0, -1):
            print(column, end="")

        # Print right side numbers increasing
        for column in range(2, row + 1):
            print(column, end="")

        print()  # Move to the next line