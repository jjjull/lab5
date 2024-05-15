import requests

def get_weather(city):
    api_key = '523dfb40bdaebd1eb016b56596df1e9f'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    data = response.json()
    
    return data


city = 'Uzhgorod'  
weather_data = get_weather(city)

if weather_data:
    print(f"Погода в місті {city}:")
    print(f"Температура: {weather_data['main']['temp']}°C")
    print(f"Вологість: {weather_data['main']['humidity']}%")
else:
    print("Не вдалося отримати погодні дані.")

import matplotlib.pyplot as plt

def display_weather(city, weather_data):
    if not weather_data:
        print("Не вдалося отримати погодні дані.")
        return
    
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']

   
    print(f"Погода в місті {city}:")
    print(f"Температура: {temp}°C")
    print(f"Вологість: {humidity}%")

  
    plt.figure(figsize=(8, 6))
    plt.bar(['Temperature', 'Humidity'], [temp, humidity], color=['pink', 'green'])
    plt.title(f"Погода в  {city}")
    plt.ylabel("Value")
    plt.show()


city = 'Uzhgorod'  
weather_data = get_weather(city)
display_weather(city, weather_data)