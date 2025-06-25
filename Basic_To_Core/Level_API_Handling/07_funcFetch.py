import requests
url = "https://api.freeapi.app/api/v1/public/randomusers"

def fetchUsers(page=1, limit=2):
    params = {"page": page, "limit":limit}
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
    for eachUser in users:
        email = eachUser.get("email")
        print(f"Email :- {email}")

        name = eachUser.get("name")
        title = name.get("title")
        first = name.get("first")
        last = name.get("last")
        print(f"User: {title}. {first} {last} \n")