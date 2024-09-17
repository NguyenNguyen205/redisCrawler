from crawler import crawler
def main():
    print('Start running')
    data = []
    # data = crawler.crawl()
    # print("Crawl data:")
    # print(data)
    print('Store data to redis')
    crawler.store(data)
    

if __name__ == '__main__':
    main()