# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("API_ID", "30223324"))
API_HASH = environ.get("API_HASH", "6d155dec716edbc1bff3da86948c4c37")
BOT_TOKEN = environ.get("BOT_TOKEN", "7705460603:AAFVNcTFjH8PZrIomfvzCdcGJYpzgMVKBTE")

