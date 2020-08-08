"""
This module is used to setup the program by storing the required details from the user.
"""

from configparser import ConfigParser
from pyfiglet import figlet_format
import os
from sys import exit

print(figlet_format("Weather wallpaper", font="digital"))


def already_configured():
    """
    If the configuration of the program is already done, 
    then the user will be prompted if they want to overwrite it.
    """
    if 'config.ini' in os.listdir(BASE_DIR):
        over_write = input(
            "It appears that you have already created a config file, would you like to over write it?(y/n) ").lower()
        if over_write == 'y':
            pass
        else:
            exit()


def main():
    """
    The user will be prompted to provide details like the API keys required and the exact location
    """
    open_weather_api_key = None
    while not open_weather_api_key:
        open_weather_api_key = input(
            "\nEntry Open Weather API key(Mandatory): ")

    print("\nEnter Unsplash API key(Optional)(If not set the default images will be selected): ")
    unsplash_api_key = input("Press enter to skip: ") or 'unset'

    exact_location = None
    y_or_n = ['y', 'n']
    while exact_location not in y_or_n:
        exact_location = input(
            "\nWould you like to provide exact location(Like latitude, longitude or zip code)?(y/n): ").lower()

    longitude, latitude, zip_code, country_code = 'unset', 'unset', 'unset', 'unset'

    if(exact_location == 'y'):
        location_choice = None
        l_or_z = ['l', 'z']
        while location_choice not in l_or_z:
            location_choice = input(
                "\nWhat would you like to provide? latitude, longitude or zip code with country code?(l/z): ").lower()
        if (location_choice == 'l'):
            longitude, latitude = input(
                "\nEnter space separated longitude and latitude(order matters): ").split()
        else:
            zip_code, country_code = input(
                "\nEnter space separated zip and country code(order matters): ").split()
    else:
        print("Then the weather will be determined based on your IP address")

    config['configuration'] = {
        "o_api": open_weather_api_key,
        'un_api': unsplash_api_key,
        'long': longitude,
        'lat': latitude,
        'zip_c': zip_code,
        'country_c': country_code
    }


if __name__ == "__main__":
    ABSOLUTE_DIR = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(ABSOLUTE_DIR)

    already_configured()
    config = ConfigParser()
    main()
    with open('./config.ini', 'w') as f:
        config.write(f)
