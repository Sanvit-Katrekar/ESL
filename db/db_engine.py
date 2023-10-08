from sqlmodel import create_engine
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

MYSQL_USERNAME = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

engine = create_engine(
    f'mysql+mysqlconnector://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}',
    pool_pre_ping=True
)