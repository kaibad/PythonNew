# Problem: Create a function that takes two numbers as parameters and returns their sum.

inputOne =int(input("Enter the First Number: "))
inputTwo =int(input("Enter the Second Number: "))

def add_two_num(numOne,numTwo):
    return numOne + numTwo

result = add_two_num(inputOne,inputTwo)
print(f"The sum of {inputOne} and {inputTwo} is {result}")