import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_weather(city):
    api_key = os.getenv("API_KEY")
    url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": city}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {data['current']['temp_c']} °C")
        print(f"Condition: {data['current']['condition']['text']}")
    else:
        print("Failed to fetch weather data.")

city = input("Enter your city: ")
get_weather(city)