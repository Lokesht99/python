# example 1
import json
with open('data.json') as f:
   data = json.load(f)
print(data)
# ----------------------------------------
# example2
# import json
#
# person = '{"name": "Bob", "languages": ["English", "French"]}'
# person_dict = json.loads(person)
#
# # Output: {'name': 'Bob', 'languages': ['English', 'French']}
# print( person_dict)
#
# # Output: ['English', 'French']
# print(person_dict['name'])
# -----------------------------------------------------------
# import json
#
# person_dict = {'name': 'Bob',
# 'age': 12,
# 'children': None
# }
# person_json = json.dumps(person_dict)
#
# # Output: {"name": "Bob", "age": 12, "children": null}
# print(person_json)
# --------------------------------------------------------
# import json
#
# person_dict = {"name": "Bob",
# "languages": ["English", "French"],
# "married": True,
# "age": 32
# }
# with open('person.txt', 'w') as json_file:
#   json.dump(person_dict, json_file,indent=4)
# ---------------------------------------------------
#Example 5
#Python pretty print JSON
# import json
#
# person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'
#
# # Getting dictionary
# person_dict = json.loads(person_string)
#
# # Pretty Printing JSON string back
# print(json.dumps(person_dict, indent = 4))
# -----------------------------------------------------------
#Example 6
# Python program to update JSON
# import json
#
# # JSON data:
# x = '{ "organization":"JKTECH","city":"Bangalore","country":"India"}'
#
# # python object to be appended
# y = {"pin":110096}
#
# # parsing JSON string:
# z = json.loads(x)
#
# # appending the data
# z.update(y)
#
# # the result is a JSON string:
# print(json.dumps(z))
# -------------------------------------------------
import json
# function to add to JSON
def func(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["employee"].append(new_data)
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)

# python object to be appended
y = {
         "id": "06",
         "name": "lokesh",
         "department": "develop",
      }

func(y)





