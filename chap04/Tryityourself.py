#4.1
pizzas = ['pepparoni','chicken','meaty']
for pizza in pizzas: 
    print (f"i like {pizza} pizza")

#4.2
animals = ['shark','dolphine','orca']
for animal in animals:
	print (f"a {animal} is a marine animal")

#4.3
for value in range(1,21):
	print(value)

#4.4
#numbers = [value**1 for value in range(1,1000000)]
#print (numbers)

#4.5
numbers = [value**1 for value in range(1,1000000)]
print (min(numbers))
print (max(numbers))
print (sum(numbers))

#4.6
odd_numbers = list(range(1,20))
for number in 