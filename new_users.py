current_users = ['Josh', 'jenny', 'harry', 'amy', 'kevin', 'admin']
new_users = ['kyle', 'Janna', 'berry', 'AMY', 'josh']

current_users_lower = [user.lower() for user in current_users]

if new_users:
	for new_user in new_users:
		if new_user.lower() not in current_users_lower:
			print(f'{new_user}: this username is available!')
		else:
			print(f'{new_user}: Sorry this username is already taken')

else:
	print('Please enter a username')
