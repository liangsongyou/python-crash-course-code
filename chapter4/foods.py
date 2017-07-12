my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

# showing that each list is a separate list
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print("{}".format(my_foods))

print("\nMy friend's favorite foods are:")
print("{}".format(friend_foods))