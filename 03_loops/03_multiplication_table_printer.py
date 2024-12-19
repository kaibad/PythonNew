# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

# solution
number_to_find_table=int(input("Please enter the number you want find the multiplication table of: "))

#here range(1,11) can also be written but i want it begin from 0 to 10 so i didnt incliude the 1 and by default it is from 0 to 10
for i in range(11):
    if i ==5:
        continue
    print(number_to_find_table," X" ,i," = ",number_to_find_table*i)

