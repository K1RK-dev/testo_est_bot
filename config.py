import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
FP_TOKEN = os.getenv("FP_TOKEN")
