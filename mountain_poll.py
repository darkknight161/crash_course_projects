responses = {}

polling_active = True

while polling_active:
	name = input('\nWhat is your name?  ')
	response = input('Which mountain would you like to climb today?  ')

	responses['name'] = response
	