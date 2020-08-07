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


print(get_full_picture("cold"))
