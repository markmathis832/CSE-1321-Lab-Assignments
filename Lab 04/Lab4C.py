# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: 4C


# Program Lab4C.py
# create a program that prompts the user for the three sides of
# a triangle and then determines what type of triangle the user has

# User input
first = int(input("Enter the first side of the triangle: "))
second = int(input("Enter the second side of the triangle: "))
third = int(input("Enter the third side of the triangle: "))

if first > 0 and second > 0 and third > 0:

    if first + second > third and first + third > second and second + third > first:

        if first == second == third:
            print("The triangle is an equilateral triangle.")
        elif first == second or first == third or second == third:
            print("The triangle is an isosceles triangle.")
        else:
            print("The triangle is a scalene triangle.")

    else:
        print("The sides do not form a valid triangle.")

else:
    print("Invalid input. All sides must be greater than 0.")