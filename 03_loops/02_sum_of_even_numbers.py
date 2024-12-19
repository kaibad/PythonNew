# Problem: Calculate the sum of even numbers up to a given number n.
n=int(input("Enter the value of n:"))
sum_of_even_numbers=0
for i in range(n+1):
    if i % 2 == 0:
        # print(i,"is even number")
        sum_of_even_numbers +=i

print(f"The sum of even number upto {n} is : {sum_of_even_numbers}")