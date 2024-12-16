# Problem: Suggest an activity based on the season (e.g., Summer - Go swimming, Winter - Skiing). Use nested conditionals to handle temperature ranges within seasons.x``
from datetime import datetime

current_date= datetime.today()
current_month=current_date.month
# print(current_month)

#determine the season on the basis of the current month
if current_month in [12,1,2]:
    season="Winter"
    activity="Skiing"
elif current_month in  [3,4,5]:
    season ="Spring"
    activity="Plant some flower ot  take some natural walk"
elif current_month in [6,7,8]:
    season="Summer"
    activity="Go Swimming"
else:
    season="Autumn"
    activity="Take a scenic drive to enjoy the fall foliage."

print(f'Season is {season} and the suggested activity to do is "{activity}"')