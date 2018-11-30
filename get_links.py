import requests
from bs4 import BeautifulSoup

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