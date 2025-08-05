# JSON File Handling
# Write a Python program to:
# - Create a dictionary with some key-value pairs:
#     data = {"name": "John", "age": 30, "skills": ["Python", "JavaScript"]}
# - Save the dictionary to a file 'data.json'
# - Read it back and print the contents

import json


data ={
  "name":"John",
  "age":30,
  "skills":[
      "Python",
      "JavaScript",
  ],
 }

# Write dictionary to 'data.json'
with open ("data.json",'w') as file:
    json.dump(data, file, indent=4)
    file.close()


# Read back the content from 'data.json'
with open('data.json','r') as file:
    loaded_data=json.load(file)
    print(loaded_data)
    file.close()


# json.dump() vs. json.dumps():
# json.dump() writes Python data to a file-like object, while json.dumps() returns a JSON formatted string.

# json.load() vs. json.loads():
# json.load() reads JSON data from a file-like object, while json.loads() parses a JSON formatted string.