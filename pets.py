pets = [{
	'name': 'sunny',
	'species': 'dog',
	'weight': 42,
	'color': 'black',
	'owner': 'brandie park',
	}, {
	'name': 'pancake',
	'species': 'gecko',
	'weight': .01,
	'color': 'brown',
	'owner': 'addy park',
	}, {
	'name': 'pierre',
	'species': 'dog',
	'weight': 22,
	'color': 'gray',
	'owner': 'ron wilson',
	}, {
	'name': 'macie',
	'species': 'dog',
	'weight': 10,
	'color': 'black',
	'owner': 'amy king',
	}, {
	'name': 'skiba',
	'species': 'dog',
	'weight': 25,
	'color': 'black and white',
	'owner': 'kelly wilson',
	}
]

for pet in pets:
	print(f"{pet['owner'].title()}'s pet is a {pet['color']} {pet['species']} named"\
	f" {pet['name'].title()} who is {pet['color']} and weighs {pet['weight']} pounds!")