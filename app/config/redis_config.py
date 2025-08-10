import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join (dirname(__file__), '.env')
load_dotenv(dotenv_path)

REDIS_CONFIG = {
   "host" : os.environ.get("REDIS_HOST"),
   "port" : int(os.environ.get("REDIS_PORT")),
   "password" : os.environ.get("REDIS_PASSWORD"),
}