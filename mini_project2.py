import requests
from bs4 import BeautifulSoup

proxy = 'http://wwwproxy.kanazawa-it.ac.jp:8080'











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
