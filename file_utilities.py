import os
from urllib.parse import urlparse

import requests


def get_file_extension(file_path):
    parsed = urlparse(file_path)
    path = os.path.splitext(parsed[2])
    return path[1]


def save_image_file(directory, image_url, file_name):
    image_response = requests.get(image_url)
    image_response.raise_for_status()
    extension = get_file_extension(image_url)
    with open(f'{directory}{file_name}{extension}', 'wb') as file:
        file.write(image_response.content)
