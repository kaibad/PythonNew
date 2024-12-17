# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).
year_to_be_checked=int(input("Enter the year you want to check.. ").strip())
if(year_to_be_checked%4==0 and year_to_be_checked%100!=0 or year_to_be_checked%400==0):
    is_leap=True
    print(f"{year_to_be_checked} is Leap Year")
else:
    is_leap=False
    print(f"{year_to_be_checked} is not Leap Year")


    
