# Problem: Create a lambda function to compute the cube of a number.

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# syntax
# lambda arguments : expression

inputNum=float(input("Enter the number: "))

cube = lambda inputNum: inputNum ** 3

print(cube(inputNum))

