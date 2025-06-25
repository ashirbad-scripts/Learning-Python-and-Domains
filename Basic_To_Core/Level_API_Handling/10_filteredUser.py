import requests
url = "https://api.freeapi.app/api/v1/public/randomusers"

# CAN BE RUN AT SAMETIME
print("\n")
print("FILTER BASED ON GENDER = MALE")
print("-------------------------------->\n")
def fetchUsers(page=3, limit=10):
    params = {"page": page, "limit" : limit}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    except requests.RequestException as e:
        print(f"Error occured: {e}")
        return None
    
data = fetchUsers()
if data:
    users = data.get("data", {}).get("data", [])
    maleUsers = [eachUser for eachUser in users if eachUser.get("gender") == "male"]

    for eachUser in maleUsers:
        name = eachUser.get("name")
        title = name.get("title")
        first = name.get("first")
        last = name.get("last")
        gender = eachUser.get("gender")

        print(f"Name: {title}. {first} {last}, gender: {gender}")
        

# --------------------------------------------------------------------------------
print("\n")
print("FILTER BASED ON COUNTRY = INDIA")
print("---------------------------------->\n")

def fetchUsers2(page=1, limit=10):
    params = {"page": page, "limit" : limit}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    except requests.RequestException as e:
        print(f"Error occured: {e}")
        return None
data = fetchUsers2()
if data:
    users = data.get("data", {}).get("data", [])
    filteredUsers = [eachUser for eachUser in users if eachUser.get("location").get("country") == "India"]

    for eachUser in filteredUsers:
        # name = eachUser.get("name")
        f = eachUser.get("name").get("first")
        l = eachUser.get("name").get("last")
        c = eachUser.get("location").get("country")

        print(f"User: {f} {l}, country: {c}")