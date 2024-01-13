import requests
import re
from bs4 import BeautifulSoup


def scrape(url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    title = soup.find('title').text
    date = soup.find('div', class_='text-cnn_grey text-sm mb-4').text
    media_artikel = soup.select_one('div.detail-image')
    image_src = None
    if media_artikel is not None:
        image_src = media_artikel.find('img')['src']
    article = soup.select_one('div.detail-text')
    pattern = re.compile(
        r'ADVERTISEMENT.*?SCROLL TO RESUME CONTENT', re.DOTALL)

    footer_pattern = re.compile(r'\[Gamb.*?\)', re.DOTALL)
    read_more_pattern = re.compile(r'Baca.*?\.', re.DOTALL)
    result = re.sub(pattern, '', article.text)
    result = re.sub(footer_pattern, '', result)
    result = re.sub(read_more_pattern, '', result)
    result = result.strip().replace('\n', ' ')
    print("Success scraping {}".format(url))
    if image_src is None:
        print("Image not found")
    return {
        'title': title,
        'date': date,
        'image_src': image_src,
        'content': result
    }
