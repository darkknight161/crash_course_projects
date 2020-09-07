available_toppings = ['mushrooms', 'onions', 'pepperoni', 'sausage', \
'pinapple', 'ham', 'extra cheese', 'green pepper']

requested_toppings = ['sausage', 'pepperoni', 'mushrooms', 'ham',\
'sour skittles']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f'Adding {requested_topping}.')
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print('\nFinished making your pizza!')

price = ''
if len(requested_toppings) == 3:
	price = 12
elif len(requested_toppings) == 4:
	price = 16
elif len(requested_toppings) == 5:
	price = 20
elif len (requested_toppings) >= 6:
	price = 30
else:
	price = 10

print(f'\nYour total for your order is ${price}')
