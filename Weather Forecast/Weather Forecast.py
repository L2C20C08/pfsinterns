import tkinter as tk
from tkinter import messagebox
import requests
import json

def get_weather():
    city_name = cityName.get()
    
    if city_name == "":
        messagebox.showerror("Input Error", "Please enter an actual city")
        return
    
    
    api_Key = "20498a2e3f307ae5c6190c0cf9920858"
    baseURL = "https://api.openweathermap.org/data/2.5/weather?q="

    completeURL = baseURL + city_name + "&appid=" + api_Key

    try:
        response = requests.get(completeURL)
        data = response.json()
        
        if data["cod"] == 404:
            messagebox.showerror("City not found", "Please enter a valid city")
        else:
            main = data["main"]
            weather = data["weather"][0]
            wind = data["wind"]
            
            temperature = round(main["temp"] - 273.15, 2)
            feels_like = round(main["feels_like"] - 273.15, 2)
            temp_max = round(main["temp_max"] - 273.15, 2)
            temp_min = round(main["temp_min"] - 273.15, 2)
            wind_speed = round(wind["speed"], 2)

            
            result_label.config(text=f"Weather: {weather['description'].capitalize()}\n"
                                    f"Temperature: {temperature}°C\n"
                                    f"Feels Like: {feels_like}°C\n"
                                    f"Max Temp: {temp_max}°C\n"
                                    f"Min Temp: {temp_min}°C\n"
                                    f"Wind Speed: {wind_speed} m/s")

    except Exception as e:
        messagebox.showerror("API Error", f"An error occurred: {e}")


window = tk.Tk()
window.title("Weather Forecast App")
window.geometry("400x300")


label = tk.Label(window, text="Welcome to the Weather Forecast App", font=("Open Sans", 20))
label.pack(pady=10)

label = tk.Label(window, text="Enter a city: ")
label.pack(pady=5)


cityName = tk.Entry(window)
cityName.pack(pady=5)

# Button to get the weather information
get_weather_button = tk.Button(window, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

# Label to display the weather information
result_label = tk.Label(window, text="Weather information will appear here", justify="left")
result_label.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()