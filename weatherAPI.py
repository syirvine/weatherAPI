import requests
import configparser
import os
import tkinter
from tkinter import messagebox


# Read and parse the apiKey form the config.ini file, store as a variable
Config = configparser.ConfigParser()
if os.path.isfile(r'config.ini'):
    Config.read(r"config.ini")
else:
    Config.read(r"..\Config.ini")
apiKey = Config.get("apiKeys", "weather")


# Ask the user for the name of a city or town
city = input("Please enter the name of a city or town: ")
# Create a variable for the API request concatenating the city/town & API key
apiRequest = (f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}")


# Calling the weather API request
weather = requests.get(apiRequest)


# Convert to a dictionary
weatherDict = (weather.json())
print(weatherDict)


# Extrapolating weather data
listExtract = weatherDict['weather']    # weather key data stored as a dictionary at index 0 in a list
dictExtract = listExtract[0]            # Extracting the dictionary form the list

weatherType = dictExtract['description']

weatherTemp = (weatherDict['main']['temp']) - 273                   # Converting temperature from Kelvin to Celsius
weatherTempRound = int(round(weatherTemp, 0))                       # Rounding to nearest whole number

feelsLike = weatherDict['main']['feels_like'] - 273                 # Converting feels like temp to Celsius
feelsLikeRound = int(round(feelsLike, 0))

humidity = weatherDict['main']['humidity']

windSpeed = (weatherDict['wind']['speed'] / 1600) * 3600            # Converting from m/s to mph
windSpeedRound = int(round(windSpeed, 0))

cloudCoverage = weatherDict['clouds']['all']


# Prints the weather info for the user
print(f"The weather in {city} today is {weatherType}. The temperature is {weatherTempRound}°C but will feel more like \
{feelsLikeRound}°C due to a wind speed of {windSpeedRound}mph and a humidty of {humidity}%. There is cloud coverage of {cloudCoverage}%")


# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()
# Show the weather data as an alert
messagebox.showinfo(f"{city} Weather", f"The weather in {city} today is {weatherType}. The temperature is {weatherTempRound}°C but will feel more like \
{feelsLikeRound}°C due to a wind speed of {windSpeedRound}mph and a humidty of {humidity}%. There is cloud coverage of {cloudCoverage}%")