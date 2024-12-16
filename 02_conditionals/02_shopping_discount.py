# Product prices
product_list = {
    "Bottle": 200,
    "Air Buds": 3000,
    "Mouse": 200,
    "Cup": 50,
    "Mobile": 250000
}

# Input for product and loyalty program
product_name = input("Enter the name of the product: ").strip()
is_loyal_customer = input("Are you a loyalty program member? (yes/no): ").strip().lower() == "yes"

total_price = 0

# Process the first product
if product_name in product_list:
    total_price += product_list[product_name]
    print(f"The original price of {product_name}: ${product_list[product_name]}")

    # Loop to add more products
    while input("Do you want to add more products? (yes/no): ").strip().lower() == "yes":
        product_name = input("Enter the name of the product: ").strip()
        if product_name in product_list:
            total_price += product_list[product_name]
            print(f"The original price of {product_name}: ${product_list[product_name]}")
            print(f"Total price before discount: ${total_price}")
        else:
            print("Product not found in the list. Please try again.")

    # Apply discount if applicable
    if total_price >= 100 and is_loyal_customer:
        discount = total_price * 0.1
        final_price = total_price - discount
        print("You are eligible for a 10% discount")
        print(f"Before Discount: ${total_price:.2f}")
        print(f"After Discount: ${final_price:.2f}")
    else:
        print(f"No discount applies. Final price: ${total_price:.2f}")
else:
    print("Product not found in the list.")
