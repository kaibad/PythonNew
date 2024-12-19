# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

momo_list=["chicken momo","mutton momo","buff momo","pork momo", "Chicken momo"]

unique_momos=set()
# the set is unindexed so the output can be in random and we use set constructor because set only containe unique items

# print(unique_momos)

for momo in momo_list:
    if momo.lower() in unique_momos:
        print(f"{momo}  already exists")
        break
    unique_momos.add(momo.lower())
print(unique_momos)