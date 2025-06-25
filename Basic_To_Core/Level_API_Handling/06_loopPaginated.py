import requests
url = "https://api.freeapi.app/api/v1/public/randomusers"

for page in range(1,4):
    params = {
        "page" : page,
        "limit" : 2    #limits the number of users to show in page
    }
    response = requests.get(url, params=params)
    data = response.json()
    users = data.get("data", {}).get("data", [])
    print(f"Page {page} users: ")
    # Loop and print data of each page
    for eachUser in users:
        name = eachUser.get("name")
        title = name.get("title")
        firstN = name.get("first")
        LastN = name.get("last")
        email = eachUser.get("email")
        
        print(f" - Name: {title}. {firstN} {LastN}")
        print(f" -> Email: {email}")
