"""
The main module is used to start the program and 
check is the configuration is generated or not.

If the config file found then based on the details provided corresponding,
APIs are fetched
"""

import requests
import os
from set_wallpaper import download_wallpaper_with_key, set_wallpaper_without_key
from configparser import ConfigParser
from sys import exit
from pyfiglet import figlet_format


def get_weather_with_location(key, longitude=None, latitude=None, zip=None, country=None):
    """
    If exact location is provided then weather will be more accurate.

    Either latitude, longitude or zip code and country code is to be used.

    Parameters:
    key (str): The Open weather API key
    longitude (str): The longitude of the users location
    latitude (str): The latitude of the users location
    zip (str): The zip code of the users location
    country (str);the country code of the users location

    Returns:
    tuple: The description and the main weather detail
    """
    if longitude != 'unset':
        params = get_latitude_longitude(latitude, longitude, key)
    else:
        params = {"zip": f"{zip},{country}", "appid": key, 'units': 'metric'}

    r = request_api(params)

    return get_description_main(r)


def get_weather_with_ip(key):
    """
    If exact location is not provided the the location will be based on your IP address.

    Parameters:
    key (str): The Open weather API key

    Returns:
    tuple: The main and description attributes of the API
    """
    r = requests.get('https://ipinfo.io')
    latitude, longitude = r.json()['loc'].split(',')

    params = get_latitude_longitude(latitude, longitude, key)

    r = request_api(params)

    return get_description_main(r)


def get_description_main(r):
    """
    From the fetched API, the description and main weather will be parsed.

    And the weather report is printed.

    Parameters:
    r (str): The JSON fethed from the Unslpash API

    Returns:
    tuple: The main and description attributes of the API
    """
    description = r.json()['weather'][0]['description']
    main = r.json()['weather'][0]['main']

    print('Weather Report: ')
    print("Temperature: ", str(
        r.json()['main']['temp'])+u"\N{DEGREE SIGN}"+"C")
    print('Satus: ', r.json()['weather'][0]['description'].title())
    print("Humidity: ", str(r.json()['main']['humidity'])+"%")

    return main, description


def get_latitude_longitude(latitude, longitude, key):
    """
    Setting the parameters for the API with latitude and longitude.

    Parameters:
    key (str): The Open weather API key
    longitude (str): The longitude of the users location
    latitude (str): The latitude of the users location

    Returns:
    dict: A dictionary with the parameters assigned to keys  
    """
    params = {
        'lat': latitude,
        "lon": longitude,
        "appid": key,
        'units': 'metric'
    }
    return params


def request_api(params):
    """
    Requesting for the actual API.

    Parameters:
    params (dict): A dictionary with the parameters required for the API

    Returns:
    str: The fectched string in the format of JSON
    """
    return requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)


if __name__ == "__main__":
    ABSOLUTE_DIR = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(ABSOLUTE_DIR)

    if 'config.ini' not in os.listdir(BASE_DIR):
        print("Config file is not generated, run config.py first")
        exit()

    print(figlet_format("Weather wallpaper", font="digital"))
    parser = ConfigParser()
    parser.read(os.path.join(BASE_DIR, 'config.ini'))

    open_weather_map_key = parser.get('configuration', 'o_api')

    if parser.get('configuration', 'long') != 'unset' or parser.get('configuration', 'zip_c') != 'unset':

        longitude, latitude, zip_c, country = parser.get('configuration', 'long'), parser.get(
            'configuration', 'lat'), parser.get('configuration', 'zip_c'), parser.get('configuration', 'country_c')

        weather = get_weather_with_location(open_weather_map_key,
                                            longitude,
                                            latitude,
                                            zip_c,
                                            country)
    else:
        weather = get_weather_with_ip(open_weather_map_key)

    if parser.get('configuration', 'un_api') != 'unset':
        unsplash_api_key = parser.get('configuration', 'un_api')
        download_wallpaper_with_key(*weather, unsplash_api_key)
    else:
        set_wallpaper_without_key(weather[0])
