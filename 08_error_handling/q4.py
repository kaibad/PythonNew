# 4. Use try-except-else to read a number from the user and print whether it is even or odd.
# Ensure that the else block is used properly and explain its role.

def odd_even():
    try:
        num=int(input("Enter any number: ").strip())
    except ValueError:
        print("That is not a valid integer.")
    else:
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
    finally:
        return "calculation completed"

while True:
    odd_even()

    isRepeat = input("Do you want to continue? (yes/no) ").strip().lower()
    if isRepeat == 'no':
        break
