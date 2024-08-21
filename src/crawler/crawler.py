from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# import requests

from repository import redisDAO

# Crawl data
def crawl():
    print('Crawling the tenor website')
    # Set up headless driver
    service = Service(executable_path='./assets/chromedriver-win64/chromedriver.exe')
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
    items = soup.find_all('div', class_='Bm3ON', limit=1)
    for item in items:
        print(item)

# Store data to redis
def store():
    r = redisDAO.getInstance()
