travel_list = ['los angeles', 'washington', 'houston', 'france', 'sweden']

print('\nOriginal order:')
print(travel_list)

print('\nAphabetical:')
print(sorted(travel_list))

print('\nOriginal order:')
print(travel_list)

print('\nReversed Aphabetical:')
print(sorted(travel_list, reverse=True))

print('\nOriginal:')
print(travel_list)

print('\nReversed:')
travel_list.reverse()
print(travel_list)

print('\nOriginal:')
travel_list.reverse()
print(travel_list)

print('\nAphabetical:')
travel_list.sort()
print(travel_list)

print('\nReverse Aphabetical:')
travel_list.sort(reverse=True)
print(travel_list)

print('\nNumber of Locations in our Travel List:')
print(len(travel_list))

for travel_lista in travel_list:
	print(travel_lista)
