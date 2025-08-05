# Write a Python program that:
# - Creates a file named 'sample.txt'
# - Writes the following lines to it:
#   Hello, world!
#   Welcome to Python file handling.
#   This is the third line.
# - Then reads and prints the content of the file line by line.

with open('sample.txt','w') as file:
    file.write('Hello, world!\n')
    file.write('Welcome to Python file handling.\n')
    file.write('This is the third line.')
    file.close()

with open ('sample.txt','r') as file:
    content=file.read()
    print(content.strip())
    file.close()