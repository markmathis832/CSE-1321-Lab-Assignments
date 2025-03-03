# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: Lab 8B

# Program Lab8B.py
print("[Friend List]")

friends_list = []
choice = 0

while choice != 3:
    print("1 - Add friend")
    print("2 - List friends")
    print("3 - Quit")

    choice = int(input("Make your selection: "))

    if choice == 1:
        friend = input("Enter your friend's name: ")
        age = int(input("Enter your friend's age: "))
        tuple = (friend, age)
        friends_list.append(tuple)
        print("Friend added")
    elif choice == 2:
        for friend in friends_list:
            print("Name: " + friend[0] + ", Age: " + str(friend[1]))
    elif choice == 3:
        print("Shutting down...")
        break


