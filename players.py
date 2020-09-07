players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:3])
print(players[:3])
print(players[-3:])

print("\nHere are the first 3 players on my team:\n")
for player in players[:3]:
	print(player.title())
