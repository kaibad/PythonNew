# Problem: Write a program that checks if a given string is a palindrome using a loop (ignoring spaces, punctuation, and case).
# we here need to find this using the loop so we will reverse a string anf if the reversed string and the original string is same then it is pallindrome

input_str=input("Enter the string to check whether it is Pallindrome or not: ")
cleaned_text=input_str.strip().lower()
# print(cleaned_text)
reversed_string=""

for char in cleaned_text:
    reversed_string=char + reversed_string

if input_str==reversed_string:
   print(f"{input_str} is a Pallindrome")

