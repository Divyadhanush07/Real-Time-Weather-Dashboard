import requests
import tkinter as tk
from tkinter import messagebox

# Set your OpenWeatherMap API Key
api_key = "c88e18b6c6f46471475b23454f918821"

# Function to fetch current weather data
def fetch_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'description': data['weather'][0]['description']
        }
        return weather
    else:
        print("Failed to fetch data.")
        return None

# Function to update weather information in the GUI
def update_weather():
    city = city_entry.get()
    if city:
        weather = fetch_weather(city, api_key)
        if weather:
            weather_info = f"City: {weather['city']}\n"
            weather_info += f"Temperature: {weather['temperature']}°C\n"
            weather_info += f"Humidity: {weather['humidity']}%\n"
            weather_info += f"Wind Speed: {weather['wind_speed']} m/s\n"
            weather_info += f"Description: {weather['description']}"
            result_label.config(text=weather_info)
        else:
            messagebox.showerror("Error", "Could not fetch data for the specified city.")
    else:
        messagebox.showwarning("Input Required", "Please enter a city name.")

# Function to compare weather between two cities
def compare_weather():
    city1 = city_entry.get()
    city2 = city_entry_2.get()
    if city1 and city2:
        weather1 = fetch_weather(city1, api_key)
        weather2 = fetch_weather(city2, api_key)
        if weather1 and weather2:
            comparison = (f"{city1} - Temp: {weather1['temperature']}°C, "
                          f"Humidity: {weather1['humidity']}%, "
                          f"Wind Speed: {weather1['wind_speed']} m/s\n"
                          f"{city2} - Temp: {weather2['temperature']}°C, "
                          f"Humidity: {weather2['humidity']}%, "
                          f"Wind Speed: {weather2['wind_speed']} m/s")
            comparison_label.config(text=comparison)
        else:
            messagebox.showerror("Error", "Could not fetch data for one or both cities.")
    else:
        messagebox.showwarning("Input Required", "Please enter names for both cities.")

# Initialize the main window
root = tk.Tk()
root.title("Real-Time Weather Dashboard")
root.geometry("500x400")

# City input and search button for current weather
city_label = tk.Label(root, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

search_button = tk.Button(root, text="Get Weather", command=update_weather)
search_button.pack()

# Display current weather information
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack()

# Input for second city and comparison button
city_label_2 = tk.Label(root, text="Enter Second City:")
city_label_2.pack()

city_entry_2 = tk.Entry(root)
city_entry_2.pack()

compare_button = tk.Button(root, text="Compare Cities", command=compare_weather)
compare_button.pack()

# Display comparison result
comparison_label = tk.Label(root, text="", font=("Arial", 10), justify="left")
comparison_label.pack()

# Run the GUI loop
root.mainloop()
