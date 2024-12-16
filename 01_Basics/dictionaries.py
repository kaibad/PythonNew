#dict is mostly used in the non sql data while working in the project
#key and valu are here in dict but in list there is only index

mobile_companies={"apple":"iphone 16","Samsung":"Note 20","Xaomi":"MI 14"}
# print(mobile_companies)

#printing the value of the index
# print(mobile_companies["apple"])

#using the get method
# print(mobile_companies.get("Samsung"))

# for i in mobile_companies:
#     print(mobile_companies)

#ching the value of the index
mobile_companies["Samsung"]="Note 20 pro max ultra"
# print(mobile_companies)

#loop in dict
for i in mobile_companies:
    print(i)

for x in mobile_companies:
    print(x,mobile_companies[x])

for key,value in mobile_companies.items():
    print(key,value)

#if i put the value instead of the index i didnt get any output
if "apple" in mobile_companies:
    print("you got note 20 pro")

print(len(mobile_companies))

#adding the new item in the dict
mobile_companies["One Plus"]="One plus 14"
# print(mobile_companies)

mobile_companies.pop("Xaomi")
# print(mobile_companies)

#multiple dict
mobile_bazaar={
    "Samsung":{
        "a20": 12000,
        "note 20": 200000
    },
    "Apple":{
        "Iphone xs max":2000,
        "Iphone 13":200000,
        "Iphone 16":240000,
    },
    "Google":{
        "Google px 1":2000,
        "Google px 2":3440
    }
}
# print(mobile_bazaar)
print(mobile_bazaar["Samsung"]["a20"])

# Comhernsion in dict
# x:x**2 is used beacause the dict use the key/
Squared_nums={x:x**2 for x in range(6)}
print(Squared_nums)

Squared_nums.clear()
print(Squared_nums)

keys =["a20","momo","i13"]
default_values="to fetch"
new_dict = dict.fromkeys(keys ,default_values)
print(new_dict)