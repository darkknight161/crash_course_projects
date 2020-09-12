print()
print()
prompt = 'Welcome to AMC Theaters!'
prompt2 = '\nHow many tickets do you want to purchase?  '
prompt3 = '\nHow old are you?  '
print(prompt)

tickets_price = {
	'adult': 15,
	'youth': 10,
	'child': 0,
}
tickets_cost = 0
play = 'yes'

active = True

while active:
	if play == 'no':
		active = False
	else:
		tickets_num = input(prompt2)
		tickets_num = int(tickets_num)
		tickets_age = input(prompt3)
		tickets_age = int(tickets_age)
			
		if tickets_num != 0:
			if tickets_age < 3:
				tickets_cost = tickets_num * tickets_price['child']
			elif tickets_age <= 12:
				tickets_cost = tickets_num * tickets_price['youth']
			else:
				tickets_cost = tickets_num * tickets_price['adult']
		else:
			print('Please enter a number greater than 0 to order tickets, or type "no" to exit')
			play = input('\n   Would you like to place another order?  ')

		print(f'Thanks!  The cost of your tickets will be ${tickets_cost}')
		play = input('\n   Would you like to place another order?  ')

