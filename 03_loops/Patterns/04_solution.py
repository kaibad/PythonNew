# Problem: Write a nested loop to print a square pattern of numbers for a given size `n`:
# 1111
# 2222
# 3333
# 4444

n=4 #this is the number of rows
for i in range(1,n+1):
   for j in range(n):
      print(i,end="")
   print()