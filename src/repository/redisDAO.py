import redis

# connector 
r = None

def getInstance():
    if (r != None):
        return r
    try:
        r = redis.Redis(host='localhost', port=3000, decode_responses=True)
        return r
    except:
        print("Can't connect to redis")
         
