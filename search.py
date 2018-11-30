import json

filename = 'labs.json'
test_params = 'ビッグデータ'

with open(filename, mode='r', encoding='utf-8') as f:
    data = json.load(f)

for d in data:
    print(d)
    for dict in d['labs']:
        if test_params in dict['keywords']:
            print(dict['lab'])
            print('!?!?!?!??!????????????!!')
    print('------------------------------------------------------------')
