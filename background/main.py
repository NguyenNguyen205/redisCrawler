#!/usr/local/bin python                                                           
import sys
from consumer import writeBehindTask
import time, threading

def action():
    print("Reading from redis")
    data = writeBehindTask.readCache()
    if (data == []):
        print("Cache is empty")
        return;
    writeBehindTask.writeDatabase(data)

def setInterval(interval, action):
    nextTime = time.time() + interval
    stopEvent = threading.Event()
    while not stopEvent.wait(nextTime - time.time()):
        nextTime += interval
        action()     

def main():
    interval = 3
    # setInterval(interval, action)
    action()


if __name__ == '__main__':
    main()