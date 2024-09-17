import redis
import os
from dotenv import load_dotenv

dotenv_path = "./src/env/.env"
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
            RedisDAO.r = redis.Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), decode_responses=True)
            RedisDAO.r.set("Hello", "World")
            print("Connect successfully")
            return RedisDAO.r
        except:
            print("Can't connect to redis")
         
