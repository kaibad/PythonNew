# Problem: Write a loop that detects and prints any consecutive repeating elements in a list.
# e can iterate through the list and compare each element to the next one. If two consecutive elements are the same, we print that element.
#linear search

sequence = [1, 2, 2, 3, 4, 4, 4, 5]
consecutive_repeated_nums=set()
for num in range(len(sequence)-1):# Stop at the second-to-last index to avoid out of bounds error
    if sequence[num] == sequence[num + 1]:
       consecutive_repeated_nums.add(sequence[num])
        
print(consecutive_repeated_nums," and the count od the is :" , len(consecutive_repeated_nums))