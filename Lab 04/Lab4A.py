# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: 4A

# Program Lab4A.py
# Write a program that prompts the user to
# input the number grade they received on an

# User input
grade = float(input("Enter your grade: "))

# Letter Grades
if grade <= 100 and grade >= 97.1:
    print ("Letter grade is: A+")
elif grade <= 97 and grade >= 94.1:
    print ("Letter grade is: A")
elif grade <= 94 and grade >= 91.1:
    print ("Letter grade is: A-")
elif grade <= 91 and grade >= 88.1:
    print ("Letter grade is: B+")
elif grade <= 88 and grade >= 85.1:
    print ("Letter grade is: B")
elif grade <= 85 and grade >= 82.1:
    print ("Letter grade is: B-")
elif grade <= 82 and grade >= 79.1:
    print ("Letter grade is: C+")
elif grade <= 79 and grade >= 76.1:
    print ("Letter grade is: C")
elif grade <= 76 and grade >= 73.1:
    print ("Letter grade is: C-")
elif grade <= 73 and grade >= 70.1:
    print ("Letter grade is: D+")
elif grade <= 70 and grade >= 67.1:
    print ("Letter grade is: D")
elif grade <= 67 and grade >= 64.1:
    print ("Letter grade is: D-")
else:
    print ("Letter grade is: F")