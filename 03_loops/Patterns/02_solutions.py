# Problem: Write a nested loop to print the following inverted pattern for a given number of rows `n`:
# ****
# ***
# **
# *
n=int(input("Enter the Height of the Pyramid: "))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()
