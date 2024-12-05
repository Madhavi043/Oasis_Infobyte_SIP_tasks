from tkinter import *
import requests  # For user requests
from datetime import datetime    
import json  # Interface with user and access essential information

root = Tk()
root.geometry("400x500")
root.resizable(10, 10)
root.title("Weather APP-AskPython.com")

city_value = StringVar()

def show_weather():
    api_key = "dbe3fbb8799724481d1c666b246a7730"  # API key from OpenWeatherMap
    city_name = city_value.get()
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    
    response = requests.get(weather_url)
    weather_info = response.json()
    # Used to access data from the weather API
    if weather_info['cod'] == 200:  # 'cod' indicates successful response, 200 means success
        kelvin = 273
        
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6  # Convert wind speed to km/h
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        
        sunrise_time = datetime.utcfromtimestamp(sunrise + timezone).strftime('%Y-%m-%d %H:%M:%S')
        sunset_time = datetime.utcfromtimestamp(sunset + timezone).strftime('%Y-%m-%d %H:%M:%S')
        
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloudiness: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly enter a valid City Name!!"
    
    tfield.delete(1.0, END)
    tfield.insert(INSERT, weather)

# UI Components
Label(root, text='Enter City Name', font='Times 14 bold').pack(pady=10)
inp_city = Entry(root, textvariable=city_value, width=24, font='Times 14 bold')  
inp_city.pack()

Button(root, command=show_weather, text="Check Weather", font="Times 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5).pack(pady=20)

Label(root, text="The Weather is:", font='Times 12 bold').pack(pady=10)

tfield = Text(root, width=46, height=10, font='Times 10')  
tfield.pack()

root.mainloop()
