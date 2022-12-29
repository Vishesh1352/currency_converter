import os

import requests
from dotenv import load_dotenv

load_dotenv('.env')
web_int=os.environ.get("web_int")
API_KEY=os.environ.get("api_key")
url=os.environ.get("base_url")
responce=requests.get(f'{url}').json()
currencies=dict(responce['conversion_rates'])