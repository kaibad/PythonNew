# 3. Write a function that divides two numbers.
# Handle ZeroDivisionError and any other unexpected errors using multiple except blocks.
# Also, make sure to use finally to print "End of function."

def divide_two_number():
    try:
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))
        rem=num1 / num2
        return f"the remainder is {rem}"
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except ValueError:
        return "Please enter valid integers only."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    finally:
        print("End of function.")

    # print("End od Function")

x = divide_two_number()
print(x)