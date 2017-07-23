my_foods = ['pizza','falafel','carrot cake','cup cake','candy','coffee','cannoli','desserts','veges']

print("{}".format(my_foods))

print("The first three items in the list are:")
for food in my_foods[0:3]:
    print("{}".format(food))

mid = int(len(my_foods)/2)
print("Three items from the middle of the list are:")
for food in my_foods[mid: mid + 3]:
    print("{}".format(food))

print("Three items in the last of list are:")
for food in my_foods[-3:]:
    print("{}".format(food))