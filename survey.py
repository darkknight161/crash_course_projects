name_prompt = '\nWhat is your name?  '
age_prompt = 'How old are you?  '
income_prompt = 'What is your median income?  '
place_prompt = 'If you could visit one place in the world, where would'\
' you go  ?  '
continue_prompt = '\nWould you like to let another person respond? (yes / no)  '

responses = {}

polling_active = True

while polling_active:
	name = input(name_prompt)
	age = input(age_prompt)
	age = int(age)
	income = input(income_prompt)
	income = income.replace(',', '')
	income = income.replace('$', '')
	income = int(income)
	place = input(place_prompt)

	responses[name] = [age, income, place]

	repeat = input(continue_prompt)
	if repeat == 'no':
		polling_active = False	

print('\n--- Poll Results ---')
for name, place in responses.items():
	print(f"{name.title()} is {place[0]} years old and has a median income"\
	f" of ${place[1]}, and would like to visit {place[2].title()}.")