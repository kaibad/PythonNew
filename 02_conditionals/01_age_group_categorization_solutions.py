# Age Group Categorization: Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).
user_age=int(input("Enter Your Age:"))

if user_age<0:
    print("Enter Your Valid Age")
    exit()
if user_age < 13:
    print("You are child")
elif user_age<20:
    print("Your are Teenager")
elif user_age<60:
    print("You are Adult")
else:
    print("Namaste Your are a Senior")
