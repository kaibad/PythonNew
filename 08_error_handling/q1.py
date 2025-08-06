# Write a program that asks the user to enter a number and prints its square.
# Use try-except to handle the case when the input is not a valid number.

while True:
    try:
        user_input=int(input("Enter any number: "))
        square=user_input**2
        print(f"The square of {user_input} is {square}")
    except ValueError:
        print('the input is not a valid number')
    
    isRepeat=input("Do you want to continue? (yes/no) ").strip().lower()
    if(isRepeat == "no"):
        break
