cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

cars.reverse()
print(cars)
cars.sort()
print(cars)

print(len(cars))

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
