import requests

from get_file_extension import get_file_extension


def save_image_file(directory, image_url, file_name):
    image_response = requests.get(image_url)
    image_response.raise_for_status()
    extension = get_file_extension(image_url)
    with open(f'{directory}{file_name}{extension}', 'wb') as file:
        file.write(image_response.content)
