# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: 3B

# Program Lab3B.py
# Write a program that reads from the user the number of hours and quality
# points earned for four courses.

cH1 = int(input ("Course 1 hours: "))
cG1 = int(input ("Grade for course 1: "))
cH2 = int(input ("Course 2 hours: "))
cG2 = int(input ("Grade for course 2: "))
cH3 = int(input ("Course 3 hours: "))
cG3 = int(input ("Grade for course 3: "))
cH4 = int(input ("Course 4 hours: "))
cG4 = int(input ("Grade for course 4: "))

totalHours = cH1 + cH2 + cH3 + cH4
totalQualityPoints = (cH1 * cG1) + (cH2 * cG2) + (cH3 * cG3) + (cH4 * cG4)
GPA =  totalQualityPoints / totalHours
print("Total hours: " + str(totalHours))
print("Total quality points: " + str(totalQualityPoints))
print("Your GPA for this semester is " + str(round(GPA, 2)))