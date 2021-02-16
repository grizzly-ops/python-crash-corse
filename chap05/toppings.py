available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','extra cheese','pepperoni']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print (f"adding {requested_topping}")
	else:
		print (f"sorry we dont have {requested_topping}")


# if 'mushrooms' in requested_toppings:
# 	print ("adding mushrooms")

# elif 'pepperoni' in requested_toppings:
# 	print ("adding pepperoni")

# elif 'extra cheese' in requested_toppings:
# 	print ("adding extra cheese")

# else:
# 	print (f"sorry,we dont have{requested_topping}")


