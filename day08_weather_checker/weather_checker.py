# weather_checker.py

import requests

def get_weather(city):
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": "your_api_key_here",  # Replace this with your actual API key
        "q": city
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"\n🌤 Weather in {city.title()} 🌤")
        print(f"Temperature: {data['current']['temp_c']}°C")
        print(f"Condition: {data['current']['condition']['text']}")
        print(f"Humidity: {data['current']['humidity']}%")
        print(f"Feels like: {data['current']['feelslike_c']}°C")
    else:
        print("❌ Failed to fetch weather data.")

city = input("Enter your city: ")
get_weather(city)
