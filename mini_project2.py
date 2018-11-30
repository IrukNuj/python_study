import requests
import time
from bs4 import BeautifulSoup

proxy = 'http://wwwproxy.kanazawa-it.ac.jp:8080'


def get_keywords(url):
    time.sleep(0.1)
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    keywords_csv = soup.find('meta', attrs={'name': 'keywords'}).get('content')
    return keywords_csv.split(',')

def get_links(url):
    href_dict = {}
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all(class_='subjectItem')

    for l in links:
        keywords_list = []
        labs_list = []
        [keywords_list.append(lhref.get('href')) for lhref in l.select('.laboList a')]
        [labs_list.append(lhref.text) for lhref in l.select('.laboList a')]
        href_dict[l.p.text] = keywords_list
    return href_dict, labs_list



URL_BASE = 'https://kitnet.jp/laboratories/'
INDEX_URL = 'https://kitnet.jp/laboratories/index.html'
render_dict = {}
json_body = []

href_dict, labs_list = get_links(INDEX_URL)


keywords_dict = {}
for dept, labs_url in zip(href_dict.keys(), href_dict.values()):
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
    print(json_body)




# イカゴミ

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
