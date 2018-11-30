import get_keywords
import get_links

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