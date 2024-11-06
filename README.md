# Real-Time Weather Dashboard
A simple weather dashboard application built using Python and Tkinter. This app retrieves current weather data for cities worldwide using the OpenWeatherMap API and displays it in a user-friendly graphical interface. It also allows users to compare weather data between two cities, showing temperature, humidity, and wind speed side-by-side.

Features
Current Weather Lookup: Enter a city name to get real-time weather details, including temperature, humidity, wind speed, and a weather description.
City Comparison: Compare weather details between two cities.
Requirements
Python 3.x
OpenWeatherMap API Key (Sign up for a free API key at OpenWeatherMap)
Dependencies:
requests (for making HTTP requests to the API)
tkinter (for creating the graphical interface, usually included with Python)
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/Real-Time-Weather-Dashboard.git
cd Real-Time-Weather-Dashboard
Install Dependencies Use pip to install requests:

bash
Copy code
pip install requests
Set Up OpenWeatherMap API Key Open the weather_dashboard.py file and replace the placeholder with your API key:

python
Copy code
api_key = "YOUR_API_KEY_HERE"

Acknowledgments
OpenWeatherMap API: For providing global weather data.
