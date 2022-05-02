import os
import time

import telegram


def send_message(telegram_token, chat_id, timer):
    bot = telegram.Bot(token=telegram_token)
    while True:
        for root, dir, files in os.walk('C:\images', topdown=True):
            for file in files:
                time.sleep(timer)
                bot.send_document(
                    chat_id=chat_id,
                    document=open(f'{root}\{file}', 'rb')
                )
