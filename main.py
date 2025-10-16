import requests
from dotenv import load_dotenv
import os

# github actionhk

load_dotenv()

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    base_url = "http://api.weatherapi.com/v1/current.json"
    complete_url = f"{base_url}?key={api_key}&q={city}&aqi=no"
    
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        current = data['current']
        location = data['location']
        temperature = current['temp_c']
        humidity = current['humidity']
        description = current['condition']['text']
        
        return {
            "temperature": temperature,
            "humidity": humidity,
            "description": description,
            "location": location['name']
        }
    else:
        return None

def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    
    if weather_data:
        print(f"Weather in {weather_data['location']}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Description: {weather_data['description']}")
    else:
        print("City not found or API request failed.")

if __name__ == "__main__":
    main()