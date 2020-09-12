prompt = 'If you tell us who you are, we can personalize the message you see.'
prompt += '\nWhat is your first name? '

name = input(prompt)
print(f'Hello, {name}!')

age = input('How old are you? ')
age = int(age)
if age < 18:
	print('Sorry, you are not old enough to play this game.')
	message = 'quit'
else:
	print(f'\nGreat news, {name}! You are just about ready to play!  Enter "quit" at any time to end the program.')

message = ""

while message != 'quit':
	message = input('Tell me something, and I will repeat it back to you: ')
	
	if message != 'quit':
		print(message)
