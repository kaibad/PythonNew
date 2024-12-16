#list is mutable but the tuple is immutable 
#tuple in not changeble
#databses returns the tuples
# nesting can be in tuple also

nasta=("Chikecn Mom","Buff MOMO" ,"pork momo","mutton momo","fried chicken momo")
print(nasta[0])
print(nasta[-1])

# nasta[0] = "Chocolate Mom0"
# this gives an error that says 'tuple' object does not support item assignment
#that means we cannot change the ecisting  tuple  but we can add the items
print(len(nasta))
more_momo=("kera momo","mango momo")
new_momo_lists = nasta + more_momo
print(new_momo_lists)

if "Chinna Momo" in new_momo_lists:
    print("Order is Placed")
else:
    print("We are out of stock")

new_momo_lists=("kera momo","mango momo","Geda Momo","kera momo")
print(new_momo_lists.count("kera momo"))



