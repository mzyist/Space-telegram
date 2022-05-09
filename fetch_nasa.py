import datetime
import os
import pathlib

import requests
from dotenv import load_dotenv

from save_image import save_image_file


def fetch_nasa_apod(nasa_directory, nasa_token, nasa_url):
    nasa_url = f'{nasa_url}planetary/apod'
    payload = {
        'api_key': nasa_token,
        'count': apod_amount
    }
    response = requests.get(nasa_url, params=payload)
    response.raise_for_status()
    nasa_content = response.json()
    for count, content in enumerate(nasa_content):
        nasa_image = content['url']
        file_name = f'NASA_{count}'
        save_image_file(nasa_directory, nasa_image, file_name)


def fetch_epic(epic_directory, nasa_token, nasa_url):
    epic_url = f'{nasa_url}EPIC/api/natural?api_key={nasa_token}'
    epic_response = requests.get(epic_url)
    epic_response.raise_for_status()
    epic_content = epic_response.json()
    image_url_template = '{}EPIC/archive/natural/{}/png/{}.png?api_key={}'
    for count, content in enumerate(epic_content[:links_amount]):
        date_string = content['date']
        image_name = content['image']
        date = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
        format_date = date.strftime('%Y/%m/%d')
        file_name = f'EPIC_{count}'
        image_url = image_url_template.format(
            nasa_url,
            format_date,
            image_name,
            nasa_token
        )
        save_image_file(epic_directory, image_url, file_name)


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.getenv('NASA_API_TOKEN')
    nasa_directory = '/images/NASA_images/'
    epic_directory = '/images/EPIC_images/'
    pathlib.Path(epic_directory).mkdir(exist_ok=True)
    pathlib.Path(nasa_directory).mkdir(exist_ok=True)
    nasa_url = 'https://api.nasa.gov/'
    links_amount = 10
    apod_amount = 30
    fetch_epic(epic_directory, nasa_token, nasa_url)
    fetch_nasa_apod(nasa_directory, nasa_token, nasa_url)
