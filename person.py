people = [{
	'first_name': 'ian',
	'last_name': 'park',
	'age': 12,
	'city': 'east moline',
	'grade': '7th',
}, {
	'first_name': 'jonas',
	'last_name': 'park',
	'age': 9,
	'city': 'east moline',
	'grade': '4th',
}, {
	'first_name': 'brandie',
	'last_name': 'park',
	'age': 41,
	'city': 'east moline',
	'grade': "bachelor's degree",
}]

for person in people:
	print(f"\nFirst name: {person['first_name'].title()}")
	print(f"Age: {person['age']}")
	print(f"City: {person['city'].title()}")
	print(f"Grade: {person['grade']}")


#print(f"First name: {ian_park['first_name'].title()}")
#print(f"Age: {ian_park['age']}")
#print(f"City: {ian_park['city'].title()}")
#print(f"Grade: {ian_park['grade']}")