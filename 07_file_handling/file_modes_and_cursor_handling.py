# 2. File Modes and Cursor Handling
# Write a Python program to:
# - Open an existing file 'sample.txt' in append and read mode ('a+')
# - Append the line "This line is appended."
# - Move the file cursor to the beginning using seek()
# - Read and print the entire content.

with open ('sample.txt','a+') as file:
    print("Name of file is :", file.name)
    print("File handling mode is :",file.mode)
    print("Is closed ?",file.closed)

    file.write("\nThis line is appended.")
    file.seek(0)
    content=file.read()
    print(content)

    file.close()
    print("Is closed ?",file.closed)
