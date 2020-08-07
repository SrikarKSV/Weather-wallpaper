import requests
import random
import ctypes
import os


ABSOLUTE_DIR = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABSOLUTE_DIR)

headers = {"Accept-Version": "v1"}


def get_full_picture(query):

    params = {
        'page': random.randint(1, 20),
        'query': query,
        "orientation": "landscape",
        "client_id": "L0D-5L9JFKRRWqz_jxjmTO3FLYc1aFkcspKPlfQu_C8",
    }

    r = requests.get(
        'https://api.unsplash.com/search/photos',
        params=params,
        headers=headers
    )

    response = r.json()['results']
    pic = response[random.randint(0, 10)]['urls']['full']

    return pic


def get_screen_size_picture(query):

    pic = get_full_picture(query)
    user32 = ctypes.windll.user32
    width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    params = {
        'w': width,
        "h": height
    }

    with requests.get(pic, params=params, headers=headers, stream=True) as picture, open(f'{BASE_DIR}/wallpaper.jpg', 'wb') as f:
        f.write(picture.content)


ctypes.windll.user32.SystemParametersInfoW(
    20, 0, os.path.join(BASE_DIR, 'wallpaper.jpg'), 3)

print('Done')
