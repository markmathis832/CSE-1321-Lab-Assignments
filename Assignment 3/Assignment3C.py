# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: Assignment 3C

# Program Assignment3C.py

# # Write a Python program that plays an interactive "Guess the Word" game with the user. In this
# game, the user will try to guess a word by guessing one letter at a time. The program will display
# the word with some characters hidden as underscores (_). When the user guesses a correct letter,
# the corresponding underscores will be replaced by that letter. The game will continue until the
# user guesses all the letters correctly.
# You cannot use lists or arrays, but you can use the len() function. You should only use strings and
# simple loops. The program must be able to interact with the user by taking input and displaying
# results after each guess.

print("Welcome to the Guess the Word game!")

word = input("Enter a word to guess (lowercase letters only): ").lower()
print("\n" * 50)

display = ""
for char in word:
    display = display + "_"

print("The word to guess is:", end=" ")
for char in display:
    print(char, end=" ")
print()

while "_" in display:
    guess = input("Guess a letter: ").lower()
    
    if guess in word:
        new_display = ""
        for i in range(len(word)):
            if word[i] == guess:
                new_display = new_display + guess
            else:
                new_display = new_display + display[i]
        display = new_display
        print("Good guess!")
    else:
        print("Oops! That letter is not in the word.")
    
    print("The word to guess is:", end=" ")
    for char in display:
        print(char, end=" ")
    print()

print("Congratulations! You've guessed the word:", word)

