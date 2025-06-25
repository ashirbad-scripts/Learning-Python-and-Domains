import requests
url = "https://api.freeapi.app/api/v1/public/randomusers"


try:
    # set a 5sec timeout
    # The timeout parameter in requests.get() 
    # sets a time limit on how long the request should wait 
    # for a response from the server.
    response = requests.get(url, timeout=0.01)  #change 0.01 to 1 to succeed
    print("Request succeded within timeout")
except requests.Timeout:
    print("Request timed out")
