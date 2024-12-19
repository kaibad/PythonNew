# Problem: Check if a number is prime.
# a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).

#this while is added later if user enter the number that is not a whole number to restart the loop

while True:
    # Input prompt
    user_input = input("Enter the number: ")

    # Check if the input is a whole number and greater than 1
    if user_input.isdigit():
        input_num = int(user_input)
        
        if input_num <= 1:
            print("Please enter a number greater than 1.")
        else:
            # Prime number check
            is_prime = True
            for i in range(2, int(input_num**0.5) + 1):
                if input_num % i == 0:
                    is_prime = False
                    break

            # Output the result
            print(f"{input_num} is a prime number.") if is_prime else print(f"{input_num} is not a prime number.")
            break  # Exit loop after a valid prime check
    else:
        print("Please enter a whole number.")
