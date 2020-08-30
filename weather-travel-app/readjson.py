import json

# open existing json file
with open('test.json') as f:
    data = json.load(f)

# edit json file
data['languages'].append('Chinese')

# create new json file
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)