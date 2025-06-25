import requests

url = "https://api.freeapi.app/api/v1/public/randomusers"

params ={
    "page" : 1,
    "limit" : 1
}

headers = {
    "user-Agent" : "MyApp/1.0"
}

response = requests.get(url, params=params, headers=headers)
print("Status Code: ", response.status_code)
print(response.json())
