# Write a nested loop to print the following checkerboard pattern for a given size `n`:
# * * * *
#  * * *
# * * * *
#  * * *
# Hint: Alternate starting with a space for even/odd rows.

n=int(input("Enter the number of rows"))
for i in range(1,n+1):
    if i%2!=0:
        print("* " * n,end="")
    else:
        print(" "+"* "*(n-1),end="")
    print()