# Task 2: Write and Append Data to a File
# Problem Statement: Write a Python program that:
# 1. Takes user input and writes it to a file named output.txt.
# 2. Appends additional data to the same file.
# 3. Reads and displays the final content of the file.

file = open('output.txt','w')
write_file = file.write('Hello, Python!')
#print(f'Enter text to write to the file: {write_file}')
file.close()

file = open('output.txt','r')
read_file = file.read()
print(f'Enter text to write to the file: {read_file}')
print(f'Data successfully written to output.txt.')
file.close()

file = open('output.txt','a')
append_file = file.write('\nData successfully appended')
print(f'\nEnter additional text to append: Learning file handling in python')
print(f'Data successfully appended.')

print('\nFinal content of output.txt:')
print(read_file)
print('Learning file handling in python.')
file.close()