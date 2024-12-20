# Problem: Write a nested loop to print the following pattern for a given number of rows `n`:
# 1
# 22
# 333
# 4444
while True:
    n1=int(input("Enter the height of the pyramid: "))
    if n1 <=9:
        # Outer loop for each row
        for i in range(1,n1+1):
            # Inner loop for printing the same number `i` times
            for j in range(i):
                print(i,end="")# Print the number without a newline
            print()# Print a newline after each row
        break
    else:
        print("Enter the Number between 1 - 9 ")
        

    