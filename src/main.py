from crawler import crawler
def main():
    print('Start running')
    data = []
    print("Crawling data")
    data = crawler.crawl()
    print('Store data to redis')
    crawler.store(data)
    

if __name__ == '__main__':
    main()