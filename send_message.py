import os
import time

import telegram
from dotenv import load_dotenv


def send_message(telegram_token, chat_id, timer):
    bot = telegram.Bot(token=telegram_token)
    while True:
        for root, dir, files in os.walk('\images', topdown=True):
            for file in files:
                bot.send_photo(
                    chat_id=chat_id,
                    photo=open(f'{root}\{file}', 'rb')
                )
                time.sleep(timer)


if __name__ == "__main__":
    load_dotenv()
    telegram_token = os.getenv('TG_TOKEN')
    timer = int(os.getenv('TIMER'))
    chat_id = os.getenv('CHAT_ID')
    send_message(telegram_token, chat_id, timer)
