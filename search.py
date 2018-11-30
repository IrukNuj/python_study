import json

filename = 'labs.json'
test_params = 'データマイニング'

with open(filename, mode='r', encoding='utf-8') as f:
    data = json.load(f)

result_list = []

for d in data:
    for dict in d['labs']:
        if test_params in dict['keywords']:
            result_list.append(tuple([d['dept'], dict['lab']]))

print(result_list)