# Problem: Write a nested loop to print the following pyramid pattern for a given number of rows `n`:
#    1
#   121
#  12321
# 1234321
# Hint: Combine spaces and two ranges for numbers.
n=int(input("Enter the Height or the number of rows in your pattern"))

for i in range(1,n+1): # this loop is for the row
    # print(n - i)
    print(' '* (n - i), end="" ) # here this is printing '' n-1 times to print a space
    for j in range(1,i+1): # this loop is for increasing the number
        print(j,end="")
    for j in range(i-1,0,-1):# Loop for decreasing numbers
        print(j,end="")
    print()# Move to the next line after each row