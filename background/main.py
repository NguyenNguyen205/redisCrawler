from consumer import writeBehindTask
def main():
    print("Reading from redis")
    data = writeBehindTask.readCache()
    if (data == []):
        print("Cache is empty")
        return;
    writeBehindTask.writeDatabase(data)

if __name__ == '__main__':
    main()