unconfirmed_people = ['jack','ruby','bin']
confirmed_people = []

while unconfirmed_people:
	current_people = unconfirmed_people.pop()

	print (f"verifying person:{current_people}")
	confirmed_people.append(current_people)

	print('\nthe following people have been confirmed:')
	for confirmed_people in confirmed_people:
		print(confirmed_people)
