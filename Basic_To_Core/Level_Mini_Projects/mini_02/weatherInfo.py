import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=35.69&longitude=139.69&hourly=temperature_2m"

def fetchWeather():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weatherData = response.json()
            with open("Level_11 (Mini_Projects)/mini_02/weatherData.json", "w") as f:
                json.dump(weatherData, f, indent = 4)
            print("Weather data saved successfuly")
        
        else:
            print("Failed to retrieve weather data")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occured {e}")

fetchWeather()