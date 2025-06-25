import requests
url = "https://api.freeapi.app/api/v1/public/randomusers"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print("Data fetched successfuly")

except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")

except requests.exceptions.RequestException as err:
    print(f"Request error occurred: {err}")