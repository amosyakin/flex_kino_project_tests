import os

from dotenv import load_dotenv

load_dotenv()

user_email = os.getenv('USER_EMAIL')
user_password = os.getenv('USER_PASSWORD')

domain_url = os.getenv('DOMAIN_URL')
api_v = os.getenv('API_V')

film_id = os.getenv('FILM_ID')
