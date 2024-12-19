# Problem: Keep asking the user for input until they enter a number between 1 and 10.


while True:
    input_str=int(input("Enter a number between 1 to 10: "))

    if 1 <= input_str <=10:
        print("Thanks for entering the number between 1 and 10")
        break
    else:
        print("You Failed entering the number between 1 and 10...Please try again")