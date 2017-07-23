pizzas = ['Pepperoni','Cheese','Hot sauce']
friend_pizzas = pizzas[:]

pizzas.append('Olive topping')
friend_pizzas.append('Cheese topping')

print("My favorite pizzas are:")
for pizza in pizzas:
    print("{}".format(pizza))

print("\nMy friends favorite pizzas are:")
for pizza in friend_pizzas:
    print("{}".format(pizza))