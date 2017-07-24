requested_toppings = ['mushrooms','extra cheese','green peppers','french fries']
#requested_toppings = list()
available_toppings = ['mushrooms','pepperoni','extra cheese','olives','pepperoni','pineapple','green peppers']

#for available in available_toppings:
if requested_toppings:
    for requested in requested_toppings:
        if requested in available_toppings:
            print("Adding {}".format(requested))
        else:
            print("Sorry we don't have {}".format(requested))
    print("\nFinshied making your pizza!") 
else:
    print("Are you sure you want a plain pizza?")
