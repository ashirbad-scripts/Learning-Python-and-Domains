import requests
url = "https://api.freeapi.app/api/v1/public/randomusers"


# Send query parameters with a GET request
params = {
    "page" : 2,
    "limit" : 1
}
response = requests.get(url, params=params)
data = response.json()

print("Data of page 2 with 5 users: ", data)

