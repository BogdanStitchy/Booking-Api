import os
from dotenv import load_dotenv

load_dotenv("config/.env")

DRIVER_DB = "asyncpg"
DIALECT_DB = "postgresql"
LOGIN_DB = os.environ['LOGIN_DB']
PASSWORD_DB = os.environ['PASSWORD_DB']
NAME_DB = os.environ['NAME_DB']
HOST = os.environ['HOST']
PORT = os.environ['PORT']
HASH_FUNCTION = os.environ['HASH_FUNCTION']
SECRET_KEY = os.environ['SECRET_KEY']
HOST_REDIS = os.environ['HOST_REDIS']

DATABASE_URL = f"{DIALECT_DB}+{DRIVER_DB}://{LOGIN_DB}:{PASSWORD_DB}@{HOST}:{PORT}/{NAME_DB}"
