# 2. You are opening a file using open("data.txt"). Handle the error gracefully if the file is not found, and display a custom message to the user.

def open_a_file():
    filename="data.txt"
    try:
        with open(filename,'r') as file:
            data=file.read()
            print(data)
            
    except FileNotFoundError:
        print(f"The file '{filename}' was not found. Please check the file path or name.")

open_a_file()