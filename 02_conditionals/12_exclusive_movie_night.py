# Problem: Write a conditional that allows someone into a movie night **only if** they are 18 or older **and** have a ticket, **or** they are a VIP regardless of age or ticket.
visitor_age= int(input("Enter your valid age: "))
visitor_has_ticket=input("Do you have a Ticket? (yes/no):  ").strip().lower()=="yes"
visitor_is_vip=input("Are you a VIP Persona? (yes/no): ").strip().lower()=="yes"

if (visitor_age >= 18 and visitor_has_ticket ) or visitor_is_vip:
    print("You are alowed into  the movie night")
else:
    print("Sorry the enetrance of you into the movie night is not allowed ")