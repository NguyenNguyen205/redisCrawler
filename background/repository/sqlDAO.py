import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import String, Column, Integer, Float
from model import Item

# Check to see if current path is a linux or window base
window_os = True
current_path = str(os.getcwd())
dotenv_path = "./background/env/.env"
if (current_path[0] != "D"):
    dotenv_path = "env/.env"
    window_os = False

load_dotenv(dotenv_path=dotenv_path)

class SqlDAO:
    s = None
    def __init__(self):
        pass

    @staticmethod
    def getInstance():
        if (SqlDAO.s != None):
            return SqlDAO.s
        try:
            docker_connectionString = f"mysql://{os.getenv("SQL_USER")}:{os.getenv("SQL_PASSWORD")}@{os.getenv("SQL_HOST")}:{os.getenv("SQL_PORT")}/{os.getenv("SQL_DATABASE")}"
            print(docker_connectionString)
            engine = create_engine(docker_connectionString)
            Item.Base.metadata.create_all(engine)
            Item.Session.configure(bind = engine)
            SqlDAO.s = Item.Session()
            print("Connect successfully")
            return SqlDAO.s
            
        except Exception as err:
            print("Can't connect to mysql")
            print(err)
         

