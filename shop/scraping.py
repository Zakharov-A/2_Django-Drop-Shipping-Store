import requests
from bs4 import BeautifulSoup

from main.settings import URL_SCRAPING_DOMAIN, URL_SCRAPING


"""
{
    'name': 'Труба профильная 40х20 2 мм 3м', 
    'image_url': 'https://my-website.com/30C39890-D527-427E-B573-504969456BF5.jpg', 
    'price': Decimal('493.00'), 
    'unit': 'за шт', 
    'code': '38140012'
 }
 """


def scraping():
    resp = requests.get(URL_SCRAPING, timeout=10.0)
    if resp.status_code != 200:
        raise Exception('HTTP error access!')

    data_list = []
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    blocks = soup.select('.catalog-item-card ')
    for block in blocks:
        print(f'HTML text consists of {len(block.text)} symbols')
        print(50 * '=')
        print(block.text)
        break


if __name__ == '__main__':
    scraping()
