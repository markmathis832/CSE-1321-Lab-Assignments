# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: 5C

# Program Lab5C.py
# For this lab, we will create a simple program that keeps looping until the user inputs “please”.

userInput = input('If you would like to stop this program, say "please": ')

while userInput != "please":
    userInput = input('If you would like to stop this program, say "please": ')

print("Program complete")