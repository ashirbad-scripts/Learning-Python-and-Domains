import requests
url = "https://api.freeapi.app/api/v1/public/randomusers"
params = {
    "page": 2,
    "limit" : 10
}
response = requests.get(url, params=params)
data = response.json()
users = data.get("data", {}).get("data", [])

filteredUser = [eachUser for eachUser in users if eachUser.get("gender") == "male"]
for eachUser in filteredUser:
    title = eachUser.get("name").get("title")
    first = eachUser.get("name").get("first")
    last = eachUser.get("name").get("last")

    gender = eachUser.get("gender")

    print(f"{title}. {first} {last}")
    print(f"Gender: - {gender}\n")