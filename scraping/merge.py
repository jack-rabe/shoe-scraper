import json

file_names = ['adidas_shoes.json', 'nike_shoes.json']
combined = {
        'brands': [],
        'count': 0,
        'shoes' : [],
        } 

for file_name in file_names:
    with open(f'../data/{file_name}', 'r') as f:
        data = json.load(f)
        combined['count'] += data['count']
        combined['brands'].append(data['brand'])
        combined['shoes'].append(data['shoes'])

with open(f'../data/merged_shoes.json', 'w') as f:
    json.dump(combined, f, indent=4)
