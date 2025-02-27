#!/usr/bin/env python3

import logging
from logging.handlers import RotatingFileHandler
from .env import get_env

APP_ID = get_env(
    'APP_ID', 'Enter your Oxford Dictionaries APP ID: ')
APP_KEY = get_env(
    'APP_KEY', 'Enter your Oxford Dictionaries APP KEY: ')
API_ID = int(get_env(
    'API_ID', 'Enter your telegram API ID: '))
API_HASH = get_env(
    'API_HASH', 'Enter your telegram API HASH: ')
BOT_TOKEN = get_env(
    'BOT_TOKEN', 'Enter your telegram BOT TOKEN: ')

START_TEXT = (
    "Hi. ☺️\n"
    "I am a oxford dictionary bot by @HyetelegtamBots" 
)
ERROR_404 = "No entry was found matching the selection parameters; OR an invalid filter was specified."
HELP_TEXT = /start - "search and check me alive"
                       "About"
           "Bot By :@HyetelegramBots
             
'
             )

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            'OXF_log.txt',
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
