import os
from dotenv import load_dotenv

load_dotenv()

DROPBOX_API_KEY = os.getenv('DROPBOX_API_KEY')
DROPBOX_PATH = os.getenv('DROPBOX_PATH', "/assets-goukkowebsite")
USE_MOCK_DATA = os.getenv('USE_MOCK_DATA', 'False').lower() == 'true'
