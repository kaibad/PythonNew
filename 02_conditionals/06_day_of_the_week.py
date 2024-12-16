# Problem: Output whether it is a weekday or weekend based on an input day (e.g., Monday - Weekday, Saturday - Weekend).
from datetime import datetime
day_of_the_week =datetime.today().strftime("%A")
# print(day_of_the_week)

if day_of_the_week in ["Saturday","Sunday"]:
    print("Today is Weekend")
else:
    print("Today is Weekday")