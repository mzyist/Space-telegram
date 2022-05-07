import requests
import pathlib

from save_image import save_image_file


def fetch_spacex_launch(spacex_directory, spacex_url):
    response = requests.get(spacex_url)
    response.raise_for_status()
    launches = response.json()
    for launch in reversed(launches):
        links = launch.get('links').get('flickr').get('original')
        if links:
            for count, image_link in enumerate(links):
                file_name = f'SpaceX_{count}'
                save_image_file(spacex_directory, image_link, file_name)
            break


if __name__ == "__main__":
    spacex_directory = '/images/SpaceX_images/'
    pathlib.Path(spacex_directory).mkdir(exist_ok=True)
    spacex_url = 'https://api.spacexdata.com/v4/launches/'
    fetch_spacex_launch(spacex_directory, spacex_url)
