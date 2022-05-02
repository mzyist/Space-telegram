import os.path
import pathlib

from dotenv import load_dotenv

from fetch_nasa import fetch_nasa, fetch_epic
from fetch_spacex import fetch_spacex_launch
from send_message import send_message


if __name__ == "__main__":
    load_dotenv()
    telegram_token = os.getenv('TG_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    timer = int(os.getenv('TIMER'))
    nasa_token = os.getenv('NASA_API_TOKEN')
    nasa_directory = '/images/NASA_images/'
    epic_directory = '/images/EPIC_images/'
    spacex_directory = '/images/SpaceX_images/'
    pathlib.Path(epic_directory).mkdir(exist_ok=True)
    pathlib.Path(nasa_directory).mkdir(exist_ok=True)
    pathlib.Path(spacex_directory).mkdir(exist_ok=True)
    nasa_url = 'https://api.nasa.gov/'
    spacex_url = 'https://api.spacexdata.com/v4/launches/{}'
    fetch_epic(epic_directory, nasa_token, nasa_url)
    fetch_spacex_launch(spacex_directory, spacex_url)
    fetch_nasa(nasa_directory, nasa_token, nasa_url)
    send_message(telegram_token, chat_id, timer)
