favorite_places = {
	'brandie': ['hollywood', 'santa montica', 'amellia island'],
	'josh': ['chicago', 'galena', 'dayton'],
	'ron': ['pheonix', 'chicago', 'davenport']
}

for person, places in favorite_places.items():
	print(f"\n{person.title()}'s favorite places to visit are:")
	for place in places:
		print(f"\t{place.title()}")