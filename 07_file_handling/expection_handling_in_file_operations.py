# 4. Exception Handling in File Operations
# Write a program that attempts to open a non-existing file 'missing.txt'.
# - If the file is not found, catch the exception and print "File not found!"
# - Otherwise, read and print its contents.

try:
    with open('missing.txt','r') as file:
        content=file.read()
        print(content)
except FileNotFoundError as e:
    print(f"File not found! {e}")
