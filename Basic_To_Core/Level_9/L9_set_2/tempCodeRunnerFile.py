import json
myList = [1,2,3,4]

jsonArray = json.dumps(myList)
print("Json array: ", jsonArray)

backToList= json.loads(jsonArray)
print("Back to list: ", backToList)