# 3. Handling CSV Files
# Create a CSV file named 'students.csv' with the following headers and data:
#   Name,Age,Grade
#   Alice,20,A
#   Bob,22,B
#   Charlie,21,A
# Then write a Python program to:
# - Read and display each row
# - Count how many students got grade 'A'

import csv

grade_count=0
age_count = 0

with open("students.csv","r") as file:
    csv_file=csv.reader(file)
    headers = next(csv_file)  # Skip the header row 
    # print("Reading from file:", file.name)
    for line in csv_file:
        print(line)
        if line[2].strip().upper() == 'A':
            grade_count +=1
        if int(line[1].strip()) <= 20:
            age_count +=1
    file.close()



print(f"\nTotal students with grade 'A': {grade_count} and the number of students whose age is less than 20 or is 20 is {age_count}")