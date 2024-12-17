# Problem: Write a conditional to output \"Good Morning\", \"Good Afternoon\", \"Good Evening\", or \"Good Night\" based on the hour of the day (0-23).
from datetime import datetime,time

current_time=datetime.today().time()

if time(0,0) <= current_time < time(12,0):
    greeting="Good Morning"
elif time(12,0) <= current_time < time(17,0):
    greeting="Good Afternoon"
elif time(17,0) <= current_time < time(21,0):
    greeting="Good Evening"
else:
    greeting="Good Night"

print(greeting)