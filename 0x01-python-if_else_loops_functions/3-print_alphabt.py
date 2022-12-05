#!/usr/bin/python3
"""
Print the ASCII alphabet in lowercase, not followed by a new line.
"""
for letter in range(97, 123):
    if (letter == 101):
        continue
    elif (letter == 113):
        continue
    else:
        print(f"{chr(letter)}", end="")
