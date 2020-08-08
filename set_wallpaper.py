import requests
import random
import ctypes
import os


ABSOLUTE_DIR = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABSOLUTE_DIR)


def download_wallpaper(query):
    headers = {"Accept-Version": "v1"}

    api_params = {
        'page': random.randint(1, 3),
        'query': query,
        'orientation': 'landscape',
        "client_id": os.getenv('UNSPLASH_API')
    }

    r = requests.get(
        'https://api.unsplash.com/search/photos',
        params=api_params,
        headers=headers
    )

    response = r.json()['results']
    pic = response[random.randint(0, 10)]['urls']['raw']

    print(pic)
    with requests.get(pic, stream=True) as picture, open(f'{BASE_DIR}/downloads/wallpaper.jpg', 'wb') as f:
        f.write(picture.content)

    ctypes.windll.user32.SystemParametersInfoW(
        20, 0, os.path.join(BASE_DIR, 'downloads/wallpaper.jpg'), 3)



if __name__ == "__main__":
    download_wallpaper('freezing rain')
    print('Done')
