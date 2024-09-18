from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import uuid
# import requests

from repository.redisDAO import RedisDAO

# Crawl data
def crawl():
    print('Crawling the tenor website')
    # Set up headless driver
    driverPath = './src/assets/chromedriver-win64/chromedriver.exe'
    service = Service(executable_path=driverPath)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options = options, service = service)
    # url = 'https://tenor.com/search/tom-evil-smile-gifs'
    url = 'https://www.lazada.vn/tag/tom-and-jerry/?spm=a2o4n.homepage.search.d_go&q=tom%20and%20jerry&catalog_redirect_tag=true'
    # headers = {
    #     'Content-Type': 'application/json',
    #     'accept': 'application/json',
    # }
    # page = requests.get(url)
    browser.get(url)
    page = browser.page_source
    soup = BeautifulSoup(page, "html.parser")
    items = soup.find_all('div', class_='qmXQo', limit=3)

    mid = {}
    data = []
    # id = uuid.uuid4()
    # imageLink = items[0].contents[0].contents[0].contents[0].contents[0].contents[0]['src']
    # name = items[0].contents[1].contents[1].contents[0].text
    # price = items[0].contents[1].contents[2].contents[0].text
    # print(imageLink)
    # print(name)
    # print(price)
    for item in items:
        mid["id"] = uuid.uuid4()
        mid["name"] = item.contents[1].contents[1].contents[0].text
        mid["image"] = item.contents[0].contents[0].contents[0].contents[0].contents[0]['src']
        mid["price"] = item.contents[1].contents[2].contents[0].text

        data.append(mid)
        mid = {}

    print(data)
    return data

# Store data to redis
def store(data):
    r = RedisDAO.getInstance()
    # for d in data:
    #     r.hset(str(d["id"]), mapping = {
    #         'name': d["name"],
    #         'image': d["image"],
    #         'price': d["price"]
    #     })        
    if (r == None):
        return

    print(r.keys())
    # r.set("hello", "world")
    # print(r.get("hello"))
    

    

    
    


