from configs import Config
from app.utils.logger import console

from time import sleep
from requests import get

def self_ping():
    sleep(10)
    while True:
        if Config.RENDER_EXTERNAL_URL:
            try:
                get(f"{Config.RENDER_EXTERNAL_URL}/ping", timeout=10)
            except Exception as e:
                console.error(e)
        sleep(10 * 60)