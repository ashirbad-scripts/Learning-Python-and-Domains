import requests
url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"

# BASIC GET REQUEST
response = requests.get(url)
print("Status Code: ", response.status_code)

# PARSE A JSON RESPONSE
# print("Response Text: ", response.json())


# CHECK IS REQUEST WAS SUCCESSFUL
response = requests.get(url)
if response.status_code == 200:
    print("Request was successful")
else:
    print("Request was not successful")


# ACCESSS SPECIFIC FIELD
response = requests.get(url)
data = response.json()

users = data.get("data", {}).get("data", [])  #cuz api has two nested "data"

if users:
    firstUser = users[0]
    print("Name: ", firstUser.get("name"))
    print("Email: ", firstUser.get("email"))

# To print nested elements in api, like name is nested there
for eachItem in data["data"]["data"]:
    title = eachItem["name"]["title"]
    first_name = eachItem["name"]["first"]
    last_name = eachItem["name"]["last"]
    email = eachItem["email"]

    print(f"I am {title} {first_name} {last_name} and my email is {email}")

