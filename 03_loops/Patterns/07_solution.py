# Problem: Write a nested loop to print the following pattern for a given number of rows `n`:
# 1
# 12
# 123
# 1234
# Hint: Use a range from 1 to the current row number.
n=4

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
