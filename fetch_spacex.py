import requests
import pathlib


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


if __name__ == "__main__":
    spacex_directory = '/images/SpaceX_images/'
    pathlib.Path(spacex_directory).mkdir(exist_ok=True)
    spacex_url = 'https://api.spacexdata.com/v4/launches/{}'
    fetch_spacex_launch(spacex_directory, spacex_url)
