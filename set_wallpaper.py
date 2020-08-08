"""
This module is used to download and set the image as background.

The downloading only happens if the API key is provided, else local images are used.
"""

import requests
import random
import ctypes
import os


ABSOLUTE_DIR = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABSOLUTE_DIR)


def download_wallpaper_with_key(main, description, key):
    """
    Using the API key for the Unsplash API, images are downloaded.

    Description is used for the search query in the API.

    Parameters:
    main (str): The main attribute of the Unsplash API for weather detail
    description (str): The description attribute of the Unsplash API for weather description
    key (str): The Unsplash API key
    """
    try:
        headers = {"Accept-Version": "v1"}

        api_params = {
            'query': description,
            'orientation': 'landscape',
            "client_id": key
        }

        r = requests.get(
            'https://api.unsplash.com/search/photos',
            params=api_params,
            headers=headers
        )

        """
        The list of the images are accessed from the API
        """
        response = r.json()['results']
        pic = response[random.randint(0, 10)]['urls']['full']

        with requests.get(pic, stream=True) as picture, open(os.path.join(BASE_DIR, 'wallpaper.jpg'), 'wb') as f:
            f.write(picture.content)

        ctypes.windll.user32.SystemParametersInfoW(
            20, 0, os.path.join(BASE_DIR, 'wallpaper.jpg'), 3)

    except Exception as e:
        print("There was an error while fetching or downloading the image")
        print("The Error:", e)
        print("Reverting and using defalut images")
        set_wallpaper_without_key(main)


def set_wallpaper_without_key(main):
    """
    When there is no Unsplash API key or if the fetching of image failed, 
    then local images are used.

    Main attribute of the API is used to decide which image will be set as background

    Parameters:
    main (str): The main attribute of the Unsplash API for weather detail
    """
    if main == "Mist":
        main = "Fog"
    DEFAULT_IMAGES_FOLDER = os.path.join(BASE_DIR, "Default images", main)
    images_list = os.listdir(DEFAULT_IMAGES_FOLDER)
    random_image = images_list[random.randint(0, len(images_list) - 1)]
    ctypes.windll.user32.SystemParametersInfoW(
        20, 0, os.path.join(DEFAULT_IMAGES_FOLDER, random_image), 3)
