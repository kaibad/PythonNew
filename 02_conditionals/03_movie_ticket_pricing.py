#Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
from datetime import datetime

user_age= int(input("Enter you age."))
adult_price= 12
childern_price= 8
wednesday_dicount= 2

#datetime.today() gets the current date and time.
#strftime("%A") formats the date object to display the full name of the weekday (e.g., "Monday", "Tuesday").

# today = datetime.today()
# day_of_week ="Wednesday"
day_of_week=datetime.today().strftime("%A")

# print(today)
# print(day_of_week)

if user_age >= 18:
    ticket_price= adult_price
else:
    ticket_price=childern_price

if day_of_week == "Wednesday":
    ticket_price -= wednesday_dicount

print(f"the price for the movie is {ticket_price}")

