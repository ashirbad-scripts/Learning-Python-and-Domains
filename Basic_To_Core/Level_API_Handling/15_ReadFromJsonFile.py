# NO API JUST READ FROM JSON FILE
import json
with open("Level_10 (API_Handling)/Storing_Files/L14.json", "r") as file:
    data = json.load(file)

users = data.get("data", {}).get("data", [])
for eachUser in users:
    title = eachUser.get("name").get("title")
    first = eachUser.get("name").get("first")
    last = eachUser.get("name").get("last")

    email = eachUser.get("email")
    username = eachUser.get("login").get("username")

    print(f"Name: {title}. {first} {last}")
    print(f"username: {username}")
    print(f"Email : {email}\n")
    
print("Data read complete.")