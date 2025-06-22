import requests
postData = {"username" : "willow", "status" : "active"}
response = requests.post("https://httpbin.org/post", json=postData)
print(response.json())
print(response.json()['json'])


