# Problem: Write a nested loop to print the following zigzag number pattern for a given number of rows `n`:
# 1
# 21
# 321
# 4321
# Hint: Reverse the range for each row.

n=4
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end="")
    print()