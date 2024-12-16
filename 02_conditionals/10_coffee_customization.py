# Problem: Customize a coffee order: \"Small\", \"Medium\", or \"Large\" with an option for \"Extra shot\" of espresso.
coffee_price_list={
    "Small":3.00,
    "Medium":4.00,
    "Large":5.00
}
extra_shot_price=1.18

#Display Menu
print("Our Menu")
for coffee,price in coffee_price_list.items():
    print(f"{coffee}: ${price}")

#user input
size_of_coffee=input("Please enter the size of the coffee:").strip().capitalize()

if size_of_coffee not in coffee_price_list:
    print("Invalid coffee size. Please choose from Small, Medium, or Large.")
else:
    print(f"Extra shot Price: ${extra_shot_price}")
    extra_shot=input("Do you want the Extra Shot? (yes/no) :").strip().lower()=="yes"

    price=coffee_price_list[size_of_coffee]

    if extra_shot:
        price += extra_shot_price
        print(f"Extra shot of espresso added. ${extra_shot_price:.2f} added to your order.")

    print(f"Your {size_of_coffee} coffee with{' an extra shot' if extra_shot  else ''} costs ${price:.2f}.")
