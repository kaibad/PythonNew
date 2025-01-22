# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(user="user"):
    if not user.strip(): # Check if input is empty or just spaces
        user='user'
    return 'Hello ' + user + ' !'

userInput=input("Enter Your Name: ")

print(greet(userInput))