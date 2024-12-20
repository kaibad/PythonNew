# Problem: Write a nested loop to print the following hollow square pattern for a given size `n`:
# *****
# *   *
# *   *
# *****
# Hint: Print full stars for the first and last row, otherwise print borders with spaces.
n=int(input("Enter the height ot the no of rows in the hollow square: "))
for i in range(1,n+1):
    if i==1 or i==n:
        print("*"* n)
    else:
        print("*"+" "*(n-2)+"*")
    