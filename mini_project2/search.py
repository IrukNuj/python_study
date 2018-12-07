import json


def search_labs(params):
    filename = 'labs.json'

    with open(filename, mode='r', encoding='utf-8') as f:
        data = json.load(f)

    result_list = []

    for d in data:
        for dict in d['labs']:
            if params in dict['keywords']:
                result_list.append(tuple([d['dept'], dict['lab']]))

    return result_list