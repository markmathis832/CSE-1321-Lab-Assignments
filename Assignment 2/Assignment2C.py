# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: Assignment2C

# Program Assignment2C.py
# Your task is to develop a text-based Role-Playing Game (RPG) in Python. The game will allow the
# player to choose a character class and perform specific actions based on their selection. The
# program must provide clear instructions, handle input effectively, and display appropriate
# responses for valid and invalid choices.

# Welcome Message and Class Selection
print("Welcome to the RPG Game!")
print("Choose your class: 1. Warrior 2. Mage 3. Healer")
choice = int(input("Enter the number of your class (1/2/3): "))

match choice:
    case 1:
        print("You have chosen Warrior! You are strong and brave.")
        print("What would you like to do? 1. Attack your sword 2. Defend with your shield")

        action = int(input("Choose your action (1/2): "))

        match action:
            case 1:
                print("You swing your sword and defeat the enemy!")
                print("Thank you for playing!")
            case 2:
                print("You raise your shield and block the enemy's attack!")
                print("Thank you for playing!")
            case _:
                print("Invalid action choice. The game ends.")
                print("Thank you for playing!")
    case 2:
        print("You have chosen Mage! You wield powerful magic.")
        print("What would you like to do? 1. Cast a fireball 2. Cast a healing spell")

        action = int(input("Choose your action (1/2): "))

        match action:
            case 1:
                print("You cast a fireball and scorch the enemy!")
                print("Thank you for playing!")
            case 2:
                print("You cast a healing spell and restore your energy.")
                print("Thank you for playing!")
            case _:
                print("Invalid action choice. The game ends.")
                print("Thank you for playing!")
    case 3:
        print("You have chosen Healer! You are kind and supportive.")
        print("What would you like to do? 1. Heal your ally 2. Attack with your staff")

        action = int(input("Choose your action (1/2): "))

        match action:
            case 1:
                print("You heal your ally and boost their morale!")
                print("Thank you for playing!")
            case 2:
                print("You swing your staff and knock out the enemy!")
                print("Thank you for playing!")
            case _:
                print("Invalid action choice. The game ends.")
                print("Thank you for playing!")
    case _:
        print("Invalid class choice. The game ends.")
        print("Thank you for playing!")