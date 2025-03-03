# Class: CSE 1321L
# Section: W02
# Term: Spring 2025
# Instructor: Muhammad Usman
# Name: Mark Mathis
# Lab: Assignment 3B

# Program Assignment3B.py

# Assignment3B: Count Character Frequency

# Write a Python program that takes a string as input and counts how many times each character
# appears, ignoring spaces. Once a character's frequency has been counted, replace it with a
# number to avoid recounting it.

# For this task:

# You cannot use lists or dictionaries to store frequencies as we have not covered yet.

# You cannot use the len() function. Iterate on string sequence

# You are allowed to use the replace () function to modify the string.
# The replace () function in Python is used to replace parts of a string with a new substring.
# The syntax is: string.replace(old, new).
# old: the char you want to replace.
# new: the char you want to replace it with.

# Note:
# Space is also a character, and we don't want to count the frequency of space. You can think about
# getting rid of spaces by using replace function described above.

# Take care of upper and lower cases.

# Example runs are shown below. The user input is shown in red and bold (Notice the difference
# between time & times)

print("[Character Frequencies]")
text = input("Enter a string: ").lower()  
processed = text.replace(" ", "")  
counted_chars = ""  

for char in processed:
    if char in counted_chars:
        continue
        
    count = 0
    for current_char in processed:
        if current_char == char:
            count += 1
            
    if count > 0:
        word = "time" if count == 1 else "times"
        print(char + " appears " + str(count) + " " + word)
        counted_chars = counted_chars + char  







