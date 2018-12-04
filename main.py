import json
import requests
import time
from bs4 import BeautifulSoup

URL_BASE = 'https://kitnet.jp/laboratories/'
INDEX_URL = 'https://kitnet.jp/laboratories/index.html'


def get_keywords(url):
    time.sleep(0.5)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    keywords_csv = soup.find('meta', attrs={'name': 'keywords'}).get('content')
    return keywords_csv.split(',')


def get_links(url):
    href_dict = {}
    labs_list = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all(class_='subjectItem')

    for l in links:
        keywords_list = []
        lab_list = []
        [keywords_list.append(lhref.get('href')) for lhref in l.select('.laboList a')]
        [lab_list.append(lhref.text) for lhref in l.select('.laboList a')]
        href_dict[l.p.text] = keywords_list
        labs_list.append(lab_list)
    return href_dict, labs_list


def scrape_labs():
    json_body = []

    href_dict, labs_list = get_links(INDEX_URL)

    for dept, labs_url, labs_list in zip(href_dict.keys(), href_dict.values(), labs_list):
        labs_dict = {}
        labs_value_list = []
        for lab_url, lab in zip(labs_url, labs_list):
            labs_value_dict = {}
            url = URL_BASE + lab_url
            labs_value_dict['keywords'] = get_keywords(url)
            labs_value_dict['lab'] = lab
            labs_value_list.append(labs_value_dict)
        labs_dict['dept'] = dept
        labs_dict['labs'] = labs_value_list
        json_body.append(labs_dict)
        filename = 'labs.json'
        with open(filename, mode='w', encoding='utf-8') as f:
            # json.dump(json_body, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ':　'))
            json.dump(json_body, f, ensure_ascii=False)


def search_labs(params):
    filename = 'labs.json'

    with open(filename, mode='r', encoding='utf-8') as f:
        data = json.load(f)

    result_list = []

    for d in data:
        for dict in d['labs']:
            if params in dict['keywords']:
                result_list.append(tuple([d['dept'], dict['lab']]))
