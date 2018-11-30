import requests
import time
from bs4 import BeautifulSoup

def get_keywords(url):
    time.sleep(0.0)
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    keywords_csv = soup.find('meta', attrs={'name': 'keywords'}).get('content')
    return keywords_csv.split(',')