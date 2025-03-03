# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: Assignment 4B

# Program Assignment4B.py

def check_length(password):
    return len(password) >= 8

def check_upper_lower(password):
    lower = any(char.islower() for char in password)
    upper = any(char.isupper() for char in password)
    return lower and upper

def check_special_character(password):
    special = "!@#"
    return any(char in special for char in password)

while True:

    password = input("Enter a password: ")
    errors = "Password does not meet the requirements: "

    if not check_length(password):
        errors += " Must be at least 8 characters long."
    if not check_upper_lower(password):
        errors += " Must contain both uppercase andlowercase letters."
    if not check_special_character(password):
        errors += " Must include at least one special character (!, @, #)."


    if errors != "Password does not meet the requirements: ":
        print(errors)
    else:
        print("Password is strong!")
        break