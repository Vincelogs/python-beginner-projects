## 🐍 **Day 9: Virtual Environments + pip + Smart API Usage**

### 📘 What You Learn:

* What `pip` is and how to install Python packages
* How to create & activate a virtual environment (`venv`)
* Using `.env` files to hide sensitive keys (API keys, tokens)
* Writing cleaner code with external libraries (`requests`, `python-dotenv`, `json`)

---

### 🧠 Concepts:

#### 🔧 Virtual Environment:

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

#### 📦 Install Packages:

```bash
pip install requests python-dotenv
```

#### 📄 .env File Example:

```env
API_KEY=your_weatherapi_key_here
```

#### 📄 Use `dotenv` in Your Python Script:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
```

---

### 🛠️ Mini Project: **Cleaner Weather App with Environment Variables**
## How to Run
1. Clone repo
    ```
    git clone https://github.com/vincelogs/python-beginner-projects.git
    cd python-beginner-projects
    cd day09_env_weather_app
    ```
2. Create virtual environment:
   `python -m venv venv && source venv/bin/activate # or venv\Scripts\activate on Windows`
3. Install dependencies:
   `pip install -r requirements.txt`
4. Run:
   `python smart_weather_checker.py`

## Tools Used
- Python 3
- requests
- python-dotenv
