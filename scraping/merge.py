import json

file_names = ['adidas_shoes.json', 'nike_shoes.json', 'hoka_shoes.json', 'new_balance_shoes.json', 'brooks_shoes.json']
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
        combined['shoes'] += (data['shoes'])

with open(f'../data/merged_shoes.json', 'w') as f:
    json.dump(combined, f, indent=4)
