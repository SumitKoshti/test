# importing the libraris
import datetime as dt
import requests
import json

# construct the url
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = input("Enter your api key: ")
CITY = input("Enter a city name: ")

# main url
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

# normalize the temperature
def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

# fetching the required fields
temp_kelvin = response["main"]["temp"]
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response["main"]["feels_like"]
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response["wind"]["speed"] 
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]
sunrise_time = dt.datetime.utcfromtimestamp(response["sys"]["sunrise"] + response["timezone"])
sunset_time = dt.datetime.utcfromtimestamp(response["sys"]["sunset"] + response["timezone"])

# printing the result
print(f"Temperature in {CITY}: {temp_celsius: .2f}C or {temp_fahrenheit: .2f}F")
print(f"Temperature in {CITY}: feels like: {feels_like_celsius: .2f}C or {feels_like_fahrenheit: .2f}F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}m/s")
print(f"Sun Risees in {CITY}: {sunrise_time}local time.")
print(f"Sun Sets in {CITY}: {sunset_time}local time.")
print(f"General Weather in {CITY}: {description}")
