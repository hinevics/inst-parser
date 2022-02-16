import os
from dotenv import load_dotenv

load_dotenv()

PATH_GECKODRIVER = os.getenv('PATH_GECKODRIVER')
PASSWORD = os.getenv('PASSWORD')
USER_NAME = os.getenv('USER_NAME')
