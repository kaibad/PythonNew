# Problem: Write a function to calculate and return the square of a number.
#  function definition that is why we use def in py
# num inside the bracket us parameter

number=int(input("Enter the Number: "))

def square_of_num(num):
    # print(num ** 2)
    return number ** 2

result = square_of_num(number)
print(result)