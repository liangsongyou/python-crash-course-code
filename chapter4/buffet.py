foods = ('BBQ','Sushi','Cannoli','Coffee','Burgers')

for food in foods:
    print("{}".format(food))

# this doesn't work because tuples can't be mutated in part
#foods[1] = 'Salad'

# changing any item in a tuple requires whole reassignment

foods = ('BBQ','Salad','Cannoli','Coffee','Pizza')
print("We have updated our menu to include the following:")
for food in foods:
    print("{}".format(food))