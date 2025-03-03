# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: Assignment 4A

# Program Assignment4A.py

def format_word(word):
    return word.capitalize()

def convert_to_pascal_case(text):
    words = text.split() 
    formatted_words = [format_word(word) for word in words]
    return "".join(formatted_words)
    
text = input("Enter a string: ")
print(convert_to_pascal_case(text))


