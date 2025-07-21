# Task 1: Read a File and Handle Errors
# Problem Statement:  Write a Python program that:
# 1. Opens and reads a text file named sample.txt.
# 2. Prints its content line by line.
# 3. Handles errors gracefully if the file does not exist.

try:
    file = open('Sample.txt', 'r')
    reading_file = file.read()
    print(reading_file)

    file1 = open('Sample1.txt', 'r')
    reading_file = file1.read()
except FileNotFoundError:
    print('Error: The file Sample1.txt was not found.')
    file.close()