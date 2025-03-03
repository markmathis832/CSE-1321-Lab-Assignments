# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: Assignment 4C

# Program Assignment4C.py

from . import A4C_Functions

print("Welcome to the ATM!")

name = input("Please enter your name: ")

balance = 0

balance = float(input("Please enter your balance: $"))


option = A4C_Functions.Display_Main_Menu()

while option != 4:
    if option == 1:
        balance = A4C_Functions.Deposit(balance)
        print("Deposited $")
    elif option == 2:
        balance = A4C_Functions.Withdraw(balance)
    elif option == 3:
        balance = A4C_Functions.Check_Balance(balance)
        print("Current balance: $" + str(balance))
    
    option = A4C_Functions.Display_Main_Menu()

print("Goodbye, " + name + "! Thank you for using the ATM.")







