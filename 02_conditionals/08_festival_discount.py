# Problem: Calculate the price of a product during a festival. Apply a 15% discount only if the purchase is made between 6 PM and midnight.
from datetime import datetime,time
our_products={
    "Shocks": 40,
    "Shoes": 400,
    "Dalle": 200,
    "Yomari":70
}
    
print("Our Products: ")
for product, price in our_products.items():
    print(f"{product}: ${price}")
selected_products_by_customer= input("Select the product from the above list.").strip()


if selected_products_by_customer not in our_products:
    print("Please Select the Procuct that are available in our list")
else:
    purchased_time=datetime.today().time()
    # purchased_time=time(19,0)
    discount_start_time= time(18,0) #this is 6 pm
    discount_end_time=time(23,59,59) # this is 12AM
    if discount_start_time <= purchased_time <= discount_end_time:
        print("15 % DISCOUNT IS APPLICABLE NOW")
        discounted_price=our_products[selected_products_by_customer] * 0.85
        print(f"The price of {selected_products_by_customer} after discount is ${discounted_price:.2f}")
    else:
        print("Discount hours are not opened yet")
        print(f"The price of {selected_products_by_customer} after discount is ${our_products[selected_products_by_customer]:.2f}")


