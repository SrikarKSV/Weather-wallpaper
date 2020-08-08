import requests
import random
import ctypes
import os


ABSOLUTE_DIR = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABSOLUTE_DIR)


def download_wallpaper(main, description):
    try:
        headers = {"Accept-Version": "v1"}

        api_params = {
            'query': description,
            'orientation': 'landscape',
            "client_id": os.getenv('UNSPLASH_API')
        }

        r = requests.get(
            'https://api.unsplash.com/search/photos',
            params=api_params,
            headers=headers
        )

        response = r.json()['results']
        pic = response[random.randint(0, 10)]['urls']['full']

        print(pic)
        with requests.get(pic, stream=True) as picture, open(f'{BASE_DIR}/wallpaper.jpg', 'wb') as f:
            f.write(picture.content)

        ctypes.windll.user32.SystemParametersInfoW(
            20, 0, os.path.join(BASE_DIR, 'wallpaper.jpg'), 3)

        os.remove(f'{BASE_DIR}/wallpaper.jpg')
    except:
        if main == "Mist":
            main = "Fog"
        DEFAULT_IMAGES_FOLDER = os.path.join(BASE_DIR, "Default images", main)
        images_list = os.listdir(DEFAULT_IMAGES_FOLDER)
        random_image = images_list[random.randint(0, len(images_list) - 1)]
        ctypes.windll.user32.SystemParametersInfoW(
            20, 0, os.path.join(DEFAULT_IMAGES_FOLDER, random_image), 3)


if __name__ == "__main__":
    download_wallpaper('Fog', 'foggy')
    print('Done')
