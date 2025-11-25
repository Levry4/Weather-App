from coordinates import get_coordinates
from weather_api_service import get_weather

def main():
    city = input("Введите название города: ")
    try:
        latitude, longitude = get_coordinates(city)
        weather = get_weather(latitude, longitude)

        print(f"Погода в городе {weather['city']}:")
        print(f"Температура: {weather['temperature']}°C (ощущается как {weather['feels_like']}°C)")
        print(f"Влажность: {weather['humidity']}%")
        print(f"Давление: {weather['pressure']} гПа")
        print(f"Описание: {weather['weather_description']}")
        print(f"Скорость ветра: {weather['wind_speed']} м/с")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
