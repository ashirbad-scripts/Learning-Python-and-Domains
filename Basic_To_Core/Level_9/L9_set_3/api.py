# Use the requests library to make a GET request to a public API
import requests
response = requests.get("https://api.agify.io?name=michael")
print(response)
print(response.json())

#  Extract the JSON response from the API and access a value inside it
data = response.json()
print("Name: ", data["name"])
print("Age: ", data["age"])

# Pass parameters in a GET request using params dictionary
params = {"name" : "alice"}
response = requests.get("https://api.agify.io", params=params)
print(response.json())


# Send data via POST request using requests.
# post() and json= argument
import requests
postData = {"username" : "willow", "status" : "active"}
response = requests.post("https://httpbin.org/post", json=postData)
print(response.json())
print(response.json()['json'])




#  Handle errors (404, 500) using requests.status_code
badResponse = requests.get('https://api.agify.io/unknown-endpoint')
if badResponse.status_code != 200:
    print("Error: ", badResponse.status_code)

