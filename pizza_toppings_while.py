prompt = "Welcome to Zingo Pizza!  Let's start with Toppings!"
prompt += "\nType quit at any time when you're done with your pizza masterpiece!"
prompt += "\nWhat's your name?  "

name = input(prompt)
print(f'Hello {name}!')

toppings = []
topping = ""

while topping != 'quit':
	topping = input('Name a topping to add: ')
	if topping == 'quit':
		break
	else:
		toppings.append(topping)

print(f"Got it, {name}!  Here's a run down of what you've ordered:")
for value in toppings:
	print(value)