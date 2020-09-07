age = 65
life_stage = ''

if age < 2:
	life_stage = 'baby'
elif (age >= 2) and (age < 4):
	life_stage = 'toddler'
elif (age >=4) and (age < 13):
	life_stage = 'kid'
elif (age >= 13) and (age < 20):
	life_stage = 'teenager'
elif (age >= 20) and (age < 65):
	life_stage = 'adult'
else:
	life_stage = 'elder'

print(f'This person is a {life_stage}')
