# Space telegram

The script will download photos from SpaceX and NASA using NASA api. Then publish them on Telegram-channel

### Requirements

You need to generate API token using https://api.nasa.gov/. Token should be stored in .env file like this:
```dotenv
NASA_API_TOKEN='Paste your NASA token here'
```
Here you will also need to paste Telegram-bot token and chat id of your telegram channel:
```dotenv
TG_TOKEN='Your Telegram-bot token'
CHAT_ID='channel chat id'
```
Python3 should be already installed. Required packages listed in requirements.txt. Install them using command line:
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

Then it will publish photo on Telegram channel, one photo per 24 hour.
You can change this interval by changing variable in .env:
```dotenv
TIMER='86400' # default value in seconds is 86400
```

### API Reference

The project uses SpaceX and NASA APIs. API documentations:

* [EPIC NASA API](https://api.nasa.gov/#epic)
* [Spacex API](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1)

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
