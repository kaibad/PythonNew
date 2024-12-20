# Problem: Write a nested loop to print the following pattern for a given number of rows `n`:
# *
# **
# ***
# ****
n=int(input("Enter the Height of the Pyramid: "))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print("")