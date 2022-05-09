import os
from urllib.parse import urlparse

import requests


def get_url_extension(file_path):
    parsed = urlparse(file_path)
    path, extension = os.path.splitext(parsed.path)
    return extension


def save_image_file(directory, image_url, file_name):
    image_response = requests.get(image_url)
    image_response.raise_for_status()
    extension = get_url_extension(image_url)
    with open(f'{directory}{file_name}{extension}', 'wb') as file:
        file.write(image_response.content)
