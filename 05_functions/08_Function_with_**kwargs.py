# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# Example
# If the number of keyword arguments is unknown, add a double ** before the parameter name

# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

def key_args(**kwargs):
    # print(kwargs)
    for key,value in kwargs.items():
        print(f"{key} : {value}")

key_args(name="Suraz",age=20)
key_args(name="Kiran",age=30)
key_args(name="Aryan",age=38,Power="NoTHONG")