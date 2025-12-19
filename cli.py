import click
import json
import sys
from tabulate import tabulate

try:
    from coordinates import get_coordinates
    from weather_api_service import get_weather
except ImportError as e:
    print(f"Ошибка импорта: {e}")
    sys.exit(1)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('city')
@click.option('--units', '-u', default='metric',
              type=click.Choice(['metric', 'imperial']))
@click.option('--output', '-o', default='table',
              type=click.Choice(['table', 'json', 'short']))
def current(city, units, output):
    try:
        latitude, longitude = get_coordinates(city)
        weather_data = get_weather(latitude, longitude)
        
        if units == 'imperial':
            weather_data['temperature'] = celsius_to_fahrenheit(weather_data['temperature'])
            weather_data['feels_like'] = celsius_to_fahrenheit(weather_data['feels_like'])
            temp_unit = '°F'
            speed_unit = 'миль/ч'
        else:
            temp_unit = '°C'
            speed_unit = 'м/с'
        
        if output == 'json':
            click.echo(json.dumps(weather_data, ensure_ascii=False, indent=2))
        elif output == 'short':
            click.echo(f"{weather_data['city']}: {weather_data['temperature']}{temp_unit}, "
                      f"{weather_data['weather_description']}")
        else:
            table_data = [
                ["Город", weather_data['city']],
                ["Температура", f"{weather_data['temperature']}{temp_unit}"],
                ["Ощущается", f"{weather_data['feels_like']}{temp_unit}"],
                ["Погода", weather_data['weather_description']],
                ["Влажность", f"{weather_data['humidity']}%"],
                ["Давление", f"{weather_data['pressure']} гПа"],
                ["Ветер", f"{weather_data['wind_speed']} {speed_unit}"]
            ]
            click.echo(tabulate(table_data, tablefmt="grid"))
            
    except Exception as e:
        click.echo(f"Ошибка: {e}", err=True)

@cli.command()
@click.option('--clear', '-c', is_flag=True)
def cache(clear):
    if clear:
        get_weather.cache_clear()
        click.echo("Кэш очищен")
    else:
        cache_info = get_weather.cache_info()
        click.echo(f"Попаданий: {cache_info.hits}")
        click.echo(f"Промахов: {cache_info.misses}")
        click.echo(f"Размер: {cache_info.currsize}/{cache_info.maxsize}")

def celsius_to_fahrenheit(celsius):
    return round(celsius * 9/5 + 32, 1)

if __name__ == '__main__':
    cli()