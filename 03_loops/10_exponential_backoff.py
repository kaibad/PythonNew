# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.
# Exponential backoff is a strategy that automatically retries a failed request with increasing wait times between each attempt
import time 

wait_time=1
max_retries=5
attempts_made=0

while attempts_made < max_retries:
    print(f"Attempt {attempts_made + 1} - wait time is {wait_time} sec" )
    time.sleep(wait_time)
    wait_time *=2
    attempts_made +=1
print("Max tries Reached")

