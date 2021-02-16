favorite_numbers = {
	'lucy':[21,55],
	'jack':[81,91],
	'bob':[41,31],
	'griz':[9,12],
}

for name, numbers in favorite_numbers.items():
	print (f"\n{name.title()}'s favorite numbers are:")
	for number in numbers:
		print(f"\t{number}")
