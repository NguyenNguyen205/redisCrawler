import sqlalchemy
import os
from dotenv import load_dotenv

# Check to see if current path is a linux or window base
window_os = True
current_path = str(os.getcwd())
dotenv_path = "./background/env/.env"
if (current_path[0] != "D"):
    dotenv_path = "env/.env"
    window_os = False

load_dotenv(dotenv_path=dotenv_path)


class SqlDAO:
