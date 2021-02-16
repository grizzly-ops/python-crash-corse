human_0 = {'age':21,'hieght':132}
print (human_0['age']) 
print (human_0['hieght'])

human_0['x_position'] = 0
human_0['y_position'] = 25
print (human_0)

for age, hieght in human_0.items():
	print(f"\nKey: {age}")
	(print(f"Value: {hieght}"))