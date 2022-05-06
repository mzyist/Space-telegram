import datetime
import os
import pathlib

import requests
from dotenv import load_dotenv

from get_file_extension import get_file_extension


def fetch_nasa(nasa_directory, nasa_token, nasa_url):
    nasa_url = f'{nasa_url}planetary/apod?api_key={nasa_token}&count=30'
    response = requests.get(nasa_url)
    response.raise_for_status()
    nasa_content = response.json()
    for count, content in enumerate(nasa_content):
        nasa_image = content['url']
        nasa_get = requests.get(nasa_image)
        nasa_get.raise_for_status()
        extension = get_file_extension(nasa_image)
        with open(f'{nasa_directory}NASA{count}{extension}', 'wb') as file:
            file.write(nasa_get.content)


def fetch_epic(epic_directory, nasa_token, nasa_url):
    epic_url = f'{nasa_url}EPIC/api/natural?api_key={nasa_token}'
    epic_response = requests.get(epic_url)
    epic_response.raise_for_status()
    epic_content = epic_response.json()
    image_url_template = '{}EPIC/archive/natural/{}/png/{}.png?api_key={}'
    for count, content in enumerate(epic_content[:5]):
        date_string = content['date']
        image_name = content['image']
        date = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
        format_date = date.strftime('%Y/%m/%d')
        image_url = image_url_template.format(
            nasa_url,
            format_date,
            image_name,
            nasa_token
        )
        epic_image_request = requests.get(image_url)
        epic_image_request.raise_for_status()
        with open(f'{epic_directory}epic{count}.png', 'wb') as file:
            file.write(epic_image_request.content)



if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.getenv('NASA_API_TOKEN')
    nasa_directory = '/images/NASA_images/'
    epic_directory = '/images/EPIC_images/'
    pathlib.Path(epic_directory).mkdir(exist_ok=True)
    pathlib.Path(nasa_directory).mkdir(exist_ok=True)
    nasa_url = 'https://api.nasa.gov/'
    fetch_epic(epic_directory, nasa_token, nasa_url)
    fetch_nasa(nasa_directory, nasa_token, nasa_url)
