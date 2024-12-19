# Problem: Determine if a customer is eligible for a \"Buy One Get One Free\" offer. Criteria: Must dine in between 7 PM and 9 PM **and** order at least two main courses.
from datetime import  datetime,time
our_courses=["Chicken Tandoor","Momo","Thakali Set"]

customer_name=input("What is your name? ").strip()

print(f"Hi {customer_name}. please select form the below list")

#displaying the main courses
for food in our_courses:
    print(food)

order_time=datetime.today().time()
# order_time=time(20,0)
offer_start_time=time(19,0)
offer_end_time=time(21,0)


# this is for the number of order a user made
num_main_course=0

while True:
    order_choice=input("\nWould you like to order a main course? (yes/no): ").strip().lower()=="yes"
    if order_choice:
        food_ordered=input("Enter the name of the main course from the list: ").strip().capitalize()
        if food_ordered in our_courses:
            print(f"{food_ordered}  has been added to your order.")
            num_main_course+=1
        else:
            ("Sorry, that item is not in our menu. Please choose again.")
    elif order_choice == False:
        break
    else:
     print("Invalid choice. Please type 'yes' or 'no'.")



if offer_start_time <= order_time <= offer_end_time:
    if num_main_course>=2:
         print(f"\nCongratulations {customer_name}! You are eligible for the 'Buy One Get One Free' offer.")
    else:
        print("\nYou need to order at least two main courses to be eligible for the offer.")
else:
     print("\nThe offer is only available between 7 PM and 9 PM. Please visit during the offer hours.")
     
# Display total courses ordered
# print(f"\nTotal main courses ordered: {num_main_course}")