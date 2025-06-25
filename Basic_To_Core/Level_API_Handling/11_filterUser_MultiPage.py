import requests

url = "https://api.freeapi.app/api/v1/public/randomusers"



print("\n")
print("FILTER BASED ON GENDER = MALE")
print("-------------------------------->\n")

def fetchUsers(page=1, limit=5):
    params = {'page': page, 'limit': limit}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    except requests.RequestException as err:
        print(f"Error occured: {err}")
        return None

# applying loop for pages
for page in range(2,7):
    value = fetchUsers(page=page, limit=5)
    if value:
        users = value.get("data", {}).get("data", [])
        filteredUsers = [eachUser for eachUser in users if eachUser.get("gender") == "male"]

        print(f"\n ----- {page} -- Male users ----")
        for eachUser in filteredUsers:
            title = eachUser.get("name").get("title")
            firstName = eachUser.get("name").get("first")
            lastName = eachUser.get("name").get("last")

            email = eachUser.get("email")
            username = eachUser.get("login").get("username")
            gender = eachUser.get("gender")

            print(f"Name: {title}. {firstName} {lastName} - {gender}")
            print(f"Email: {email}")
            print(f"username: {username}\n")




# ----------------------------------------------------------------------------s
print("\n")
print("FILTER BASED ON COUNTRY = INDIA")
print("---------------------------------->\n")


def fetchUsers2(page=1, limit=5):
    params = {'page': page, 'limit': limit}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    except requests.RequestException as err:
        print(f"Error occured: {err}")
        return None

# applying loop for pages
for page in range(1,30):
    value = fetchUsers2(page=page, limit=5)
    if value:
        users = value.get("data", {}).get("data", [])
        filteredUsers = [eachUser for eachUser in users if eachUser.get("location").get("country") == "India"]

        print(f"\n ----- Data from Page {page} ----")
        if not filteredUsers:
            print("No Indian users from this page")
        
        else:
            for eachUser in filteredUsers:
                title = eachUser.get("name").get("title")
                firstName = eachUser.get("name").get("first")
                lastName = eachUser.get("name").get("last")

                email = eachUser.get("email")
                username = eachUser.get("login").get("username")

                # country = eachUser.get("location").get("country") # or
                place = eachUser.get("location")
                c = place.get("country")

                print(f"Name: {title}. {firstName} {lastName}")
                print(f"Email: {email}")
                print(f"Country: {c}")
                print(f"username: {username}\n")

