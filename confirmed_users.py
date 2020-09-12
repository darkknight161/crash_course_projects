# Start with users that need to be verified,
# and an empty list to hold confirmed users.

uncomfirmed_users = ['bart', 'maggie', 'homer', 'marge', 'lisa']
confirmed_users = []

while uncomfirmed_users:
	current_user = uncomfirmed_users.pop()

	print(f'Verifying user: {current_user}')
	confirmed_users.append(current_user)

print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
	print(confirmed_user.title())