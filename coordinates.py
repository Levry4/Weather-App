import requests
def get_coordinates(city_name):
    api_key = "dcec2117d017a73ca21c319fdf80b7a3"  
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}"

    response = requests.get(url)
    response.raise_for_status()  

    data = response.json()

    if len(data) == 0:
        raise ValueError(f"Город '{city_name}' не найден")

    latitude = data[0]['lat']
    longitude = data[0]['lon']

    return latitude, longitude


