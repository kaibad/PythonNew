# Problem: Given a string, find the first non-repeated character.
input_str=input("Enter any String: ").strip()

for char in input_str:
    char_count=input_str.count(char)
    # print("the count of ", char ," is ",char_count)
    if char_count ==1:
        print(char)
        break
        # this break prevent for checking the string after  the first non repeated charater is  found early

