import redis
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

# connector 
class RedisDAO:
    r = None
    def __init__(self):
        pass

    @staticmethod
    def getInstance():
        if (RedisDAO.r != None):
            return RedisDAO.r
        try:
            host = os.getenv("REDIS_HOST_LOCAL") if window_os else os.getenv("REDIS_HOST_DOCKER")
            RedisDAO.r = redis.Redis(host= host, port=os.getenv("REDIS_PORT"), decode_responses=True)
            RedisDAO.r.set("Hello", "World")
            print("Connect successfully")
            return RedisDAO.r
        except Exception as err:
            print("Can't connect to redis")
            print(err)
         
