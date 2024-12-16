#Problem: Check if a password is \"Weak\", \"Medium\", or \"Strong\". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
user_name=input("Enter you Username: ")
user_pass=str(input("Enter Your Password: ")).strip()
length_of_password=len(user_pass)
# print(f"The length of the password is {length_of_password}")
if length_of_password >0:
    if  length_of_password < 6:
        pass_strength="Weak"
    elif 6<= length_of_password < 10: 
     pass_strength="Medium"
    else:
        pass_strength="Strong"
    print(f"Hi ....!! {user_name} your password is too {pass_strength}")
else:
   print("Please Enter Your Password")




