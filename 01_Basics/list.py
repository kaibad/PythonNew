#just two lists
snacks_food=["sausage","fired mushroom","Mo:Mo","Pakoda","Laphing"]
drinks=["coke","sprite","dew","milk"]

#this is simple diapalting of the list using te for loop
for i in snacks_food:
    print (i)

for i in drinks:
    print(i,end="_")


#this is called comprehension of the list
# print("the request order is :")
food_selected=[x for x in snacks_food if x == "sausage"]
print(food_selected)

squared_nums = [x**2 for x in range(len(snacks_food))]
print(squared_nums)

if "dodh" in drinks:
    print("Drink is served")
else:
    print("Sorry :) we are out of stock")


#using slicing methods
momos = ["chicken","buff","mutton","pork","choila"]
print(momos[1:2])

#this below method treat the stirng "Ramen" as an array to revent for that we can use ["Ramen"]
momos[1:2]="Ramen"
# print(momos)

# append method
drinks.append("Boba tea")
print(drinks)

#pop method
drinks.pop()
drinks.pop(1)
print(drinks)

#remove method
drinks.remove("coke")
print(drinks)

#insert method
drinks.insert(1,"Coke")
print(drinks)

#copy method :by defailt the we we need to add the same in list2 as list 2 but if we do list1==list2 
#then list2 is just pinting to the memoery refrence of list one when list1 is changed the changes are seen in the list2 as well
#so in that case we use the copy method
copy_of_drinks = drinks.copy()
print(copy_of_drinks)

