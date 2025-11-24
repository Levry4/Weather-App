from coordinates import get_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather

def main():
    coordinates = get_coordinates()
    weather_data = get_weather(coordinates)
    output = format_weather(weather_data)
    print(output)

if __name__ == "__main__":
    main()
