# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: 6A

# Program 6A.py



while True:

    print()
    print("Multiplication and Exponent Calculator")
    print("Choose option 1 for Multiplication")
    print("Choose option 2 for Exponentiation")
    print("Choose option 3 to Exit")
    print()

    choice = int(input(""))

    match choice:
        case 1:

            print("Enter an operand: ", end="")
            operand1 = int(input())
            print("Enter the other operand: ", end="")
            operand2 = int(input())
            product = 0

            for _ in range(abs(operand2)):
                product += operand1

            print(str(operand1) + " x " + str(operand2) + " = " + str(product), end=" ")
            print()

        case 2:

            print("Enter the base: ", end="")
            base = int(input())
            print("Enter the exponent: ", end="")
            exponent = int(input())
            power = 1

            for _ in range(abs(exponent)):
                power *= base

            print(str(base) + "^(" + str(exponent) + ") = " + str(power), end=" ")
            print()

        case 3:
            print("Closing the Calculator...")
            break

        case _:
            print("Invalid Choice")
            print()