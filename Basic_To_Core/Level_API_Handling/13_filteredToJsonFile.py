# CHECK USER INPUT GENDER
import requests
import json

url = "https://api.freeapi.app/api/v1/public/randomusers"

def fetchUsers(page=1, limit=5):
    params = {"page": page, "limit":limit}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    except requests.RequestException as e:
        print(f"Error Occured: {e}")


genderToCheck = input("Enter (male/female) : ").strip().lower()
pageToSearch = int(input('Enter a number: ').strip())

# --- Collect all filtered users ---
all_filtered_users = []

for page in range(1, pageToSearch + 1):
    value = fetchUsers(page=page, limit=10)
    if value:
        users = value.get("data", {}).get("data", [])
        filteredUsers = [eachUser for eachUser in users if eachUser.get("gender") == genderToCheck]

        print(f"\n--- Page {page} | Users with gender '{genderToCheck}' ---")
        print("-------------------------------------------------------------->)")
        if not filteredUsers:
            print("Not found in this page")
        else:
            for eachUser in filteredUsers:
                name = eachUser.get("name")
                title = name.get("title")
                first = name.get("first")
                last = name.get("last")

                gender = eachUser.get("gender")
                username = eachUser.get("login").get("username")
                email = eachUser.get("email")
                country = eachUser.get("location").get("country")

                print(f"Name :- {title}. {first} {last}")
                print(f"Gender :- {gender}")
                print(f"Email :- {email}")
                print(f"Username :- {username}")
                print(f"Country: {country}\n")

                all_filtered_users.append(eachUser)

# To write the result to a json file
if all_filtered_users:
    with open("Level_10 (API_Handling)/Storing_Files/FilterResultJson.json", 'w') as f:
        json.dump(all_filtered_users, f, indent=4)
        print("Files dumped succesfully")
else:
    print("No matching users found")
