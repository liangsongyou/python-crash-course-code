# Store information about the pizza being ordered

pizza = {
    'crust':'thick',
    'toppings': ['mushrooms','extra cheese'],
}

# Summarize the ordering

print("You ordered a {}-crust pizza with the following toppings:".format(pizza['crust']))

for topping in pizza['toppings']:
    print("\t{}".format(topping))