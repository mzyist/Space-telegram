import datetime
import os.path
import pathlib
import time
from urllib.parse import urlparse

import requests
import telegram
from dotenv import load_dotenv

load_dotenv()
telegram_token = os.getenv('TG_TOKEN')
chat_id = os.getenv('CHAT_ID')
bot = telegram.Bot(token=telegram_token)
timer = os.getenv('TIMER')

def send_message(telegram_token, chat_id, timer):
    bot = telegram.Bot(token=telegram_token)
    for root, dir, files in os.walk('C:\images', topdown=True):
        for file in files:
            time.sleep(timer)
            bot.send_document(chat_id=chat_id, document=open(f'{root}\{file}', 'rb'))


def fetch_spacex_launch(spacex_directory, spacex_url):
    launch_id = '5eb87d42ffd86e000604b384'
    response = requests.get(spacex_url.format(launch_id))
    response.raise_for_status()
    links = response.json().get('links').get('flickr').get('original')
    for count, image_link in enumerate(links):
        image_get = requests.get(image_link)
        image_get.raise_for_status()
        with open(f'{spacex_directory}SpaceX{count}.jpg', 'wb') as file:
            file.write(image_get.content)


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


def get_file_extension(nasa_image):
    parsed = urlparse(nasa_image)
    path = os.path.splitext(parsed[2])
    return path[1]


if __name__ == "__main__":
    nasa_token = os.getenv('NASA_API_TOKEN')
    nasa_directory = '/images/NASA_images/'
    epic_directory = '/images/EPIC_images/'
    spacex_directory = '/images/SpaceX_images/'
    pathlib.Path(spacex_directory).mkdir(exist_ok=True)
    pathlib.Path(nasa_directory).mkdir(exist_ok=True)
    pathlib.Path(epic_directory).mkdir(exist_ok=True)
    spacex_url = 'https://api.spacexdata.com/v4/launches/{}'
    nasa_url = 'https://api.nasa.gov/'
    fetch_epic(epic_directory, nasa_token, nasa_url)
    fetch_spacex_launch(spacex_directory, spacex_url)
    fetch_nasa(nasa_directory, nasa_token, nasa_url)
    send_message(telegram_token, chat_id)
