import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_ID_CHAT


def send_notification(message):
	url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
	requests.post(url, data={"chat_id": TELEGRAM_ID_CHAT, "text": message})