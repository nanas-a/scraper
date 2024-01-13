import datetime
import time
import requests
from bs4 import BeautifulSoup
from service.cnbc.scraper import scraper
from config.mongo import connect as mongo_connect
from bson import ObjectId
from util.validate import validate_title, validate_url


def start(total_loop: int = 50):
    client, collection = mongo_connect()
    total_crawl = 1
    with client:
        for i in range(1, total_loop):
            try:
                url = 'https://www.cnbcindonesia.com/market/indeks/5/{}'.format(
                    i)
                print("Fetching url {}".format(url))
                page = requests.get(url)
                if page.status_code != 200:
                    print("Error while fetching url")
                    break
                soup = BeautifulSoup(page.text, 'html.parser')
                media = soup.find('ul', class_='media_rows')
                list_media = media.find_all('li')
                for index, val in enumerate(list_media):
                    link = val.find('a')['href']
                    if validate_url(link):
                        detail = scraper(link)
                        result = {
                            'link': link,
                            'source': 'cnbc indonesia',
                            'scrape_date': time.strftime("%Y-%m-%d %H:%M:%S"),
                            **detail
                        }
                        result['_id'] = str(ObjectId())
                        collection.insert_one(result)
                        print(str(total_crawl) + " Success insert " +
                              result['title']+" to database")
                        total_crawl += 1
                    else:
                        print("Data already exist")
                    print("=====================================")
            except Exception as e:
                print(e)
                print("Error while fetching url")
                continue
