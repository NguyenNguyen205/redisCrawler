from repository.redisDAO import RedisDAO
from repository.sqlDAO import SqlDAO
from model import Item

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
    s = SqlDAO.getInstance()
    if (s == None):
        print("Can't connect")
        return
    for d in data:
        item = Item.Item(name = d['name'], image = d['image'], price = d['price'])
        s.add(item)

    s.commit()
    return


    