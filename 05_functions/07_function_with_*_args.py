# Problem: Write a function that takes variable number of arguments and returns their sum.

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:

# If the number of arguments is unknown, add a * before the parameter name

# numberOfInput= int(input("How many numbers you want to add? "))
# total=0
# for i in range(numberOfInput):
#     num = float(input(f"Enter number {i+1}: "))
#     total += num

# print(f"The total sum is: {total}") 

def sum_of_all(*args):
    # print(args)
    # print(*args)
    return sum(args)

print(sum_of_all(1,2,3,4,4))