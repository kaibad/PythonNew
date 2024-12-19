# Problem: Compute the factorial of a number using a while loop.

input_num=int(input("Enter the number: "))
factorial=1;
original_num = input_num  # Save the original number for accurate display this is neede whenin the printing it is shworiing 0 because of the derement in the loop
if input_num==0:
    factorial=1
else:
    while input_num >= 0 :
        factorial*=input_num
        input_num -=1

print(f"Factorial of {original_num} is {factorial}")    

#i added the if conditional  to handle the conditon that the factorial of 0 is 1
