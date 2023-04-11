import os

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get('API_KEY', 'None')
API_SECRET_KEY = os.environ.get('API_SECRET_KEY', 'None')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', 'None')
ACCESS_SECRET_TOKEN = os.environ.get('ACCESS_SECRET_TOKEN', 'None')