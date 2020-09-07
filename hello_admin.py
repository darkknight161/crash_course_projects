username = ['josh', 'jenny', 'harry', 'amy', 'kevin', 'admin']
new_users = ['kyle', 'janna', 'berry', 'amy', 'josh']

if username:
	for name in username:
		if name == 'admin':
			print(f'Hello {name.title()}, would you like to see a status'\
			'report?')
		else:
			print(f'Hello {name.title()}, thank you for logging in again.')
else:
	print('We need some more users!')