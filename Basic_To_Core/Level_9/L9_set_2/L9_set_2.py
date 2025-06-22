# Convert a Python dictionary to a JSON string using json.dumps()
import json
data  = {'name' : 'alice', 'age' : 25}
print(data)  # single quote and can not be send for api calling
jsonString = json.dumps(data)
print(jsonString)  #double quote and can be sent for api calling


# Write a JSON string to a file using json.dump()
import json
data  = {'language' : 'python', 
         'level' : 'beginner',
         'author' : 'John'
         }
with open('L9_set_2/data.json', 'w') as f:
    json.dump(data, f)
print("Data written in 'data.json'")


# Read and convert a json file back to python object
import json
with open('L9_set_2/data.json', 'r') as f:
    result = json.load(f)
print(result)


# Parse a JSON string and extract a specific value by key
import json
jsonStr = '{"course" : "Python", "duration" : "3 months"}'
parsed = json.loads(jsonStr)
print(parsed['course'])


# Handle a malformed json string
import json
bad_json = '{"name": "John", age: 30}'
try:
    parsed = json.loads(bad_json)
except json.JSONDecodeError as e:
    print("Error: ", e)


# convert python list into Json array and back
import json
myList = [1,2,3,4]

jsonArray = json.dumps(myList)
print("Json array: ", jsonArray)

backToList= json.loads(jsonArray)
print("Back to list: ", backToList)