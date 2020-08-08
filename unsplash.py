import requests
import random
import ctypes
import os


ABSOLUTE_DIR = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABSOLUTE_DIR)


def download_wallpaper(query):
    headers = {"Accept-Version": "v1"}

    api_params = {
        'page': random.randint(1, 20),
        'query': query,
        "client_id": os.getenv('UNSPLASH_API')
    }

    r = requests.get(
        'https://api.unsplash.com/search/photos',
        params=api_params,
        headers=headers
    )

    response = r.json()['results']
    pic = response[random.randint(0, 10)]['urls']['raw']

    with requests.get(pic, stream=True) as picture, open(f'{BASE_DIR}/wallpaper.jpg', 'wb') as f:
        f.write(picture.content)


download_wallpaper('cold')

ctypes.windll.user32.SystemParametersInfoW(
    20, 0, os.path.join(BASE_DIR, 'wallpaper.jpg'), 3)

print('Done')
