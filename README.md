# Assignment4_Task-1-2
# Task 1: Read a File and Handle Errors
try:
    file = open('Sample.txt', 'r')
    reading_file = file.read()
    print(reading_file)
    file1 = open('Sample1.txt', 'r')
    reading_file = file1.read()
except FileNotFoundError:
    print('Error: The file Sample1.txt was not found.')
    file.close()

# Task 2: Write and Append Data to a File
file = open('output.txt','w')
write_file = file.write('Hello, Python!')
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
