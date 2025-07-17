## 🐍 **Day 8: Using APIs – Real-Time Weather App**

### 📘 What You Learn:

* What an API is
* How to fetch data from a public API
* JSON parsing in Python
* How to make your app interact with the outside world 🌐

---

### 🧠 Concepts:

* **API (Application Programming Interface):** A way to access data from another service
* **HTTP request:** Python sends a request, gets a response
* **JSON:** Common format returned by APIs

```python
import requests

url = "https://api.weatherapi.com/v1/current.json"
params = {
    "key": "your_api_key",
    "q": "Lagos"
}
response = requests.get(url, params=params)
data = response.json()

print(data["current"]["temp_c"])
```

---

### 🛠️ Mini Project: **Real-Time Weather Checker 🌤️**

This version uses the [WeatherAPI](https://www.weatherapi.com/) (free signup for API key).



> ⚠️ You need to replace `"your_api_key_here"` with a real one from [https://www.weatherapi.com](https://www.weatherapi.com).



