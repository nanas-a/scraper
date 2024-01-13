import datetime
import time
import requests
from bs4 import BeautifulSoup
from service.cnbc.scraper import scraper
from config.mongo import connect as mongo_connect
from bson import ObjectId
from util.validate import validate_title


def start():
    client, collection = mongo_connect()
    with client:
        for minus_day in range(30):
            date = (datetime.datetime.now() -
                    datetime.timedelta(days=minus_day)).strftime("%Y/%m/%d")
            for i in range(1, 11):
                url = 'https://www.cnbcindonesia.com/market/indeks/5/{}?date={}'.format(
                    i, date)
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
                    detail = scraper(link)
                    result = {
                        'link': link,
                        'source': 'cnbc indonesia',
                        'scrape_date': time.strftime("%Y-%m-%d %H:%M:%S"),
                        **detail
                    }
                    result['_id'] = str(ObjectId())
                    if validate_title(result['title']):
                        collection.insert_one(result)
                        print("Success insert "+result['title']+" to database")
                        time.sleep(1)
                    else:
                        print("Data already exist")
                        exit()
