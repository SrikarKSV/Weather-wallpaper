import requests
from pprint import pprint
import os
from set_wallpaper import download_wallpaper

# r = requests.get('https://ipinfo.io')


params = {
    "q":"bellary",
    "appid":os.getenv('OPEN_WEATHER_API')
}

r = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)

print(r.json()['weather'][0]['description'])
download_wallpaper(r.json()['weather'][0]['description'])
print('Done')