# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_forge in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# Show the first 5 aliens with a slice.
for alien in aliens[:5]:
	print(alien)
print('...')

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# Change the 1st 3 alien colors and speed
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

# Show first 5 aliens
for alien in aliens[:5]:
	print(alien)