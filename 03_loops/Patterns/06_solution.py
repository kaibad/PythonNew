# Problem: Write a nested loop to print the following diamond shape for a given size `n`:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# Hint: Use two loops, one for the top half and one for the bottom half.

n=4
for i in range(1,n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()