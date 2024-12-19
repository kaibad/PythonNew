# Problem: Reverse a string using a loop.
input_string=input("Enter any string: ").strip()
# print(input_string[::-1])
rev_str=""

for i in input_string:
    # rev_str +=i
    rev_str=i + rev_str
print(rev_str)

# the second method
rev_str_sec_method=""

for i in range(len(input_string)-1,-1,-1):
    rev_str_sec_method +=input_string[i]
print("this is from the second method :", rev_str_sec_method)