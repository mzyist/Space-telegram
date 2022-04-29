# Download photos from NASA

The script will download photos from SpaceX and NASA using NASA api.

### Requirements

You need to generate API token using https://api.nasa.gov/. Token should be stored in .env file like this:
```dotenv
NASA_API_TOKEN='Paste your token here'
```

Required packages listed in requirements.txt. Install them using command line:
```commandline
pip3 install -r requirements.txt
```
### How to use

To run the script simply run main.py file using command line:
```commandline
python main.py
```
It will then create 3 folders:
* /SpaceX_images
* /EPIC_images
* /NASA_images

and download photos right into them.

### API Reference

The project uses SpaceX and NASA APIs. API documentations:

* [EPIC NASA API](https://api.nasa.gov/#epic)
* [Spacex API](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1)
