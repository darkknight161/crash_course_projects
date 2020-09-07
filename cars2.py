car = 'subaru'
print('Is car == to "subaru"?  I predict True.')
print(car == 'subaru')

print('\nIs car == to "bmw"?  I prdict False.')
print(car == 'bmw')

print('\nIs car == to "Subaru"?  I predict False')
print(car == 'Subaru')

print('\nIs car == to "Subaru" when using the .title() tag?  I predict True.')
print(car.title() == 'Subaru')

vin1 = 100
vin2 = 200
vin3 = 300
vin4 = 400

vin_numbers = ['vin1', 'vin2', 'vin3', 'vin4']
print('\nAvailable VIN numbers:')
for vin in vin_numbers:
	print(f'{vin} = ')

print('\nVin2 is greater than Vin1 and less than Vin3, I predict True.')
print((vin2 > vin1) and (vin2 < vin3))

print('\nVin2 is > Vin3 or Vin4. I predict False.')
print((vin2 > vin3) or (vin2 > vin4))

print('\nVin2 is > vin1 and = to vin3. I predict False.')
print((vin2 > vin1) and (vin2 == vin3))

print("\nIs Vin1 in the list? I predict True")
print('vin1' in vin_numbers)

print('\nVin# has not been added to the list')
vin5 = 500
if vin5 not in vin_numbers:
	print('This is not a valid VIN#.  Please reenter.')

