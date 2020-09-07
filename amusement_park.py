#Requirements are as follows:
#Admission for anyone under age 4 is free
#Admission for anyone between the ages of 4 and 18 is $25
#Admission for anyone age 18 or older is $40

age = 12

if age < 4:
	print('Your admission cost is $0.')

elif (age > 4) and (age < 18):
	print('Your admission cost is $25.')

else:
	print('Your admission cost is $40.')