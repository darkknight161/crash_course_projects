#Requirements are as follows:
#Admission for anyone under age 4 is free
#Admission for anyone between the ages of 4 and 18 is $25
#Admission for anyone age 18 or older is $40

age = 65

if age < 4:
	price = 0

elif (age > 4) and (age < 18):
	price = 25

elif age >= 65:
	price = 20

else:
	price = 40

print(f'Your admission cost is ${price}.')