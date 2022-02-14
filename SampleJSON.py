# #example1
# import json
# emp='{"id":"10","name":"john"}'
# emp_dict=json.loads(emp)
# print(emp_dict)
# print(type(emp_dict))
# print("\n")
#
# json_object=json.dumps(emp_dict,indent=0)
# print(json_object)
# print(type(json_object))
#---------------------------------
#example2
# import json
# # {key:value mapping}
# a ={"name":"John","age":31,"Salary":25000}
# # conversion to JSON done by dumps() function
# b = json.dumps(a)
# # printing the output
# print(repr(b))
# print(type(b))

#------------------------------------------------
#example3
# import json
#
# # list conversion to Array
# print(json.loads('["Welcome", "to", "JSON"]'))
#
# # tuple conversion to Array
# print(json.dumps(('Welcome', "to", "JSON")))
#
# # string conversion to String
# print(json.dumps("Hi"))
#
# # int conversion to Number
# print(json.dumps(123))
#
# # float conversion to Number
# print(json.dumps(23.572))
#
# # Boolean conversion to their respective values
# print(json.dumps(True))
# print(json.dumps(False))
#
# # None value to null
# print(json.dumps(None))
# ---------------------------------------------------
# Example 4
# import json
# var = {
#       "Subjects": {
#                   "Maths":85,
#                   "computer":88,
#                   "maths":90,
#                   "English":90
#                    }
#       }
# # with open("arraySample.json", "w") as p:
# #  json.dump(var, p)
# f=open('arraySample.json','w')
# json.dump(var,f)
# f.close()
# -----------------------------------------
# #Example5
# import json
# f=open('data.json','r')
# data=json.load(f)
# for i in data['employee']:
#     print(i)
# f.close()
 # -----------------------------------------
# import json
# dict={
#         "id": "05",
#          "name": "Nancy",
#          "department": "Sales"
# }
# with open("data.json","a") as outfile:
#     json.dump(dict, outfile, indent=4)


