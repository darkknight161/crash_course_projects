favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

polling_list = ['jen', 'sarah', 'edward', 'phil', 'josh', 'brandie',\
'jonas', 'ian', 'sunny', 'natalia']

for invitee in sorted(polling_list):
	if invitee not in favorite_languages.keys():
		print(f'{invitee.title()}, please come and take our poll!')
	else:
		print(f'{invitee.title()}, thank you for taking the poll!')
