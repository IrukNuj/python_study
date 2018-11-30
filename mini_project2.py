import requests
import time
from bs4 import BeautifulSoup

proxy = 'http://wwwproxy.kanazawa-it.ac.jp:8080'


def get_keywords(url):
    time.sleep(0.5)
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    keywords_csv = soup.find('meta', attrs={'name': 'keywords'}).get('content')
    return keywords_csv.split(',')


def get_dept_and_lab(url):
    time.sleep(0.5)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    dept = soup.select_one('.subjectName p').text
    lab = soup.select_one('.laboName .title').text
    return dept, lab


render_dict = {}
render_list = []
keywords_list = []
dict_hoge = {}
url_base = 'https://kitnet.jp/laboratories/'

r = requests.get('https://kitnet.jp/laboratories/index.html')
soup = BeautifulSoup(r.content, 'lxml')

links = soup.find_all(class_='subjectItem')



for l in links:
    keywords_list = []
    labs_list = []
    [keywords_list.append(lhref.get('href')) for lhref in l.select('.laboList a')]
    [labs_list.append(lhref.text) for lhref in l.select('.laboList a')]
    dict_hoge[l.p.text] = keywords_list
    print(dict_hoge)

keywords_dict = {}
for hoge, huga in zip(dict_hoge.values(), dict_hoge.keys()):
    labs_dict = {}
    keywords_list = []
    for i, hanya in zip(hoge, labs_list):
        print('idayo-----', i)
        url = url_base + i
        keywords_dict['keywords'] = get_keywords(url)
        print(keywords_dict)
        keywords_list.append(keywords_dict)
    labs_dict['dept'] = huga
    labs_dict['labs'] = keywords_list
    print(labs_dict)






render_dict['labs'] = []

for l in links:
    if l.get('href'):
        target_url = 'https://kitnet.jp/laboratories/' + l.get('href')
        keywords = get_keywords(target_url)
        dept, lab = get_dept_and_lab(target_url)
        render_dict['dept'] = dept
        keywords_dict = {'keywords': keywords}
        # keywords_list = keywords_list.append(keywords_dict)

        print('render-dict', render_dict)
        print('keywords-dict', keywords_dict)
        print()
    # keywords_hoge = get_keywords(get_url)
    # if keywords_hoge == None:
    #     continue
    # for k in keywords_hoge:
    #     print(k)
    # r = requests.get(get_url)
    # soup = BeautifulSoup(r.content, 'lxml')
    #
    # subject_name = soup.select('.subjectName p')
    # keywords = soup.select('.keywords span')
    # titles = soup.select('.laboName .title')
    #
    # import pprint
    #
    # if subject_name:
    #     for s in subject_name:
    #         pprint.pprint("学部 : " + s.text)
    # else:
    #     continue
    #
    # keywords_list = [k.text for k in keywords]
    # pprint.pprint("キーワード : " + str(keywords_list))
    #
    # for t in titles:
    #     pprint.pprint("教授 : " + t.text)
