favorite_numbers = {
	'ian': [87, 54, 23, 10],
	'jonas': [5, 2, 4, 12],
	'brandie': [8, 88, 888, 8888],
	'sunny': [4, 5, 6, 7, 8],
	'natalia': [1, 2, 3, 10, 21],
}

#print(f"Ian's favorite number is: {favorite_numbers['ian']}")
#print(f"Jonas' favorite number is: {favorite_numbers['jonas']}")
#print(f"Brandie's favorite number is: {favorite_numbers['brandie']}")
#print(f"Sunny's favorite number is: {favorite_numbers['sunny']}")
#print(f"Natalia's favorite number is: {favorite_numbers['natalia']}")

for person, numbers in favorite_numbers.items():
		print(f"\n{person.title()}'s favorite numbers are:")
		for number in numbers:
			print(f"\t{number}")