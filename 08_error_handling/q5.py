
# 5. Define a custom exception called NegativeValueError.
# Write a function that accepts a positive integer and raises NegativeValueError if the value is negative.
# Demonstrate how to catch and handle this custom exception.

class MyCustomError(Exception):  
    pass
def accepts_pos_int():
    
    try:
        num=int(input("Enter any positive number: ").strip())
        if num < 0:
            raise MyCustomError("Number cannot be negative.")
        print(f"You entered: {num}")
    except MyCustomError as e:
         print(f"Custom Exception: {e}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    
    finally:
        print("Function execution completed.")

accepts_pos_int()