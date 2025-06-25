import requests
import json

url = "https://api.freeapi.app/api/v1/public/randomusers"

params = {
    "page" : 2,
    "limit" : 10
}

response = requests.get(url, params=params)
data  = response.json()

users = data.get("data", {}).get("data", [])
for eachUser in users:
    name = eachUser.get("name")
    title = name.get("title")
    first = name.get("first")
    last = name.get("last")


# Storing data to JSON File
with open("Level_10 (API_Handling)/Storing_Files/L14.json", "w") as f:
    json.dump(data, f, indent=4)
    print("Data dumped successfully")



