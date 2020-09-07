print("\nList 1-20:")
for value in range(1, 21):
	print(value)

print("\nProperties of list of 1 million:")
million = list(range(1, 1_000_001))
print('\nsmallest number:')
print(min(million))
print('\nlargest number:')
print(max(million))
print('\nsum of all numbers in the list:')
print(sum(million))

print('\nList of Odd numbers 1-20:')
for value in range(1, 21, 2):
	print(value)

print('\nList of multiples of 3 in a list of 1-30:')
for value in range(3, 31, 3):
	print(value)

print('\nList of the first 10 cubes:')
cube_list = []
for value in range(1, 11):
	cube_list.append(value**3)

print(cube_list)

print('\nList of the first 10 cubes with List Comprehension:')
cube_list = [value**3 for value in range(1, 11)]
print(cube_list)