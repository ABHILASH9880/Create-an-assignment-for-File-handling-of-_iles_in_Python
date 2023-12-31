# Python program showing
# use of json package
 
import json
 
# {key:value mapping}
a ={"name":"John",
   "age":31,
    "Salary":25000}
 
# conversion to JSON done by dumps() function
 b = json.dumps(a)
 
# printing the output
print(b)
# Python program showing that
# json support different primitive
# types
 
import json
 
# list conversion to Array
print(json.dumps(['Welcome', "to", "GeeksforGeeks"]))
 
# tuple conversion to Array
print(json.dumps(("Welcome", "to", "GeeksforGeeks")))
 
# string conversion to String
print(json.dumps("Hi"))
 
# int conversion to Number
print(json.dumps(123))
 
# float conversion to Number
print(json.dumps(23.572))
 
# Boolean conversion to their respective values
print(json.dumps(True))
print(json.dumps(False))
 
# None value to null
print(json.dumps(None))