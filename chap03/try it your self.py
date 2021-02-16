#3.1
name = ['jhon','levie','caroline','jacobs']
print (name[0])
print (name[1])
print (name[2])
print (name[3])

#3.2
name = ['jhon','levie','caroline','jacobs']
message =f"my bestfriend is {name[0]}"
print (message)

#3.3
cars = ['benz','BMW','audi','bently']
message = f"i would love to drive a {cars[0]}"
print (message)
message = f"i would love to drive a {cars[1]}"
print (message)
message = f"i would love to drive a {cars[2]}"
print (message)
message = f"i would love to drive a {cars[3]}"
print (message)

#3.4
people = ['hitler','obama','goku']
message = f'{people[0]} is invited to dinner'
print (message)
message = f'{people[1]} is invited to dinner'
print (message)
message = f'{people[2]} is invited to dinner'
print (message)

#3.5
people = ['hitler','obama','goku']
print ('hitler')
people = ['naruto','obama','goku']
message = f'{people[0]} is invited to dinner'
print (message)
message = f'{people[1]} is invited to dinner'
print (message)
message = f'{people[2]} is invited to dinner'
print (message)

#3.6
people = ['naruto','obama','goku']
print ('i found a bigger table')
people.insert(0,'sasuke')
people.insert(1,'gara')
people.insert(2,'vegita')
print (people)

#3.7
people = ['naruto','obama','goku']
print ('i can only invite two people')
uninvited = people.pop(2)
print (f'sorry {uninvited} you were uninvited')
message = f'{people[0]} is still invited to dinner'
print (message)
message = f'{people[1]} is still invited to dinner'
print (message)
del people [0] 
print (people)
del people [0]
print (people)

#3.8
places = ['new york','finland','new zealand','canada','russia']
print (places)
print (sorted(places))

#3.9