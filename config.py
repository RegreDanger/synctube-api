import os
from dotenv import load_dotenv

load_dotenv()

DROPBOX_API_KEY = os.getenv('DROPBOX_API_KEY')
APP_KEY = os.getenv('APP_KEY')
APP_SECRET_KEY = os.getenv('APP_SECRET_KEY')
DROPBOX_PATH = os.getenv('DROPBOX_PATH')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_ID_CHAT = os.getenv('TELEGRAM_ID_CHAT') 