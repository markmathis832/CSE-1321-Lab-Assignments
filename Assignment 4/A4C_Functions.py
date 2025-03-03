# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: Assignment 4C Functions

# Program A4C_Functions.py

def Display_Main_Menu():
    print("ATM Main Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Please choose an option (1-4): "))
    if 1 <= choice <= 4:
        return choice
    else:
        print("Invalid choice. Please try again.")
       

def Deposit(balance):
    amount = float(input("Enter the amount to deposit: "))
    balance += amount
    print("Deposited $" + str(amount) + ". New balance: $" + str(balance))
    return balance


def Withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Withdrew $" + str(amount) + ". New balance: $" + str(balance))
    return balance

def Check_Balance(balance):
    return balance


