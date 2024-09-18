from repository.redisDAO import RedisDAO
def readCache():
    data = []
    r = RedisDAO.getInstance()
    if (r == None):
        return
    
    for key in r.keys():
        if (key == "hello" or key == "Hello"):
            continue
        data.append(r.hgetall(key))
        # r.delete(key)
    
    print(data)
    return data

def writeDatabase(data):
    pass