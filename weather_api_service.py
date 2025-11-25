import os
import requests

def get_weather(latitude, longitude):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise RuntimeError("API ключ не найден! Установите переменную окружения OPENWEATHER_API_KEY")

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric&lang=ru"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    if data.get("cod") != 200:
        raise ValueError(f"Ошибка получения данных о погоде: {data.get('message', 'Неизвестная ошибка')}")

    weather_info = {
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather_description": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"],
        "city": data["name"]
    }

    return weather_info
