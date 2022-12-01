import requests
from bs4 import BeautifulSoup as BS

URL = 'https://aldebaran.ru/genre/priklucheniya/klassika-prikluchencheskoy-literatury/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

def get_html(url, params=''):
    req = requests.get(url=URL, headers=HEADERS, params=params)
    return req

def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='book_info clearfix')
    books = []
    for i in items:
        book = {
            'title': i.find('p', class_='booktitle').string,
            'link': 'https://aldebaran.ru'+i.find('p', class_='booktitle').find('a').get('href'),
        }
        books.append(book)
    return books


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        books = []
        for i in range(1,2):
            html = get_html(f'{URL}pagenum-{i}/')
            current_page = get_data(html.text)
            books.extend(current_page)
        return books
    else:
        raise Exception('Error in parser')
