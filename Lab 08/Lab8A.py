# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: Lab 8A

# Program Lab8A.py

print("[Mailing List]")

email_list = []
choice = 0

while choice != 4:

    print("1 - Add email")
    print("2 - Delete email")
    print("3 - List all emails")
    print("4 - Quit")

    choice = int(input("Make your selection: "))

    if choice == 1:
        email = input("Enter the email to be added: ")
        email_list.append(email)    
        print("Email added to mailing list.")
    elif choice == 2:
        email = input("Enter the email to be removed: ")
        if email in email_list:
            email_list.remove(email)
            print(email + " has been removed from the mailing list.")
        else:
            print("No such email in mailing list: " + email)
    elif choice == 3:
        print(email_list)
    elif choice == 4:
        print("Shutting down...")
        break
