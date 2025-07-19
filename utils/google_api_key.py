import random
import os
from dotenv import load_dotenv

MIN_VALUE = 1
MAX_VALUE = 13
load_dotenv()
def get_google_api_key():
    api_key_number = random.randint(MIN_VALUE, MAX_VALUE)
    api_key = os.getenv(f'GOOGLE_API_KEY_{api_key_number}')
    if not api_key:
        raise ValueError(f"GOOGLE_API_KEY_{api_key_number} is not set in the environment variables.")
    return api_key