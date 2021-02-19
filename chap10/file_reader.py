file_path = 'text_folder / pi_digits'
with open('text_folder/pi_digits.txt') as file_object:
	lines = file_object
	
	pi_string = ''
	for line in lines:
		pi_string += line.rstrip()
	print(pi_string)
	print(len(pi_string))