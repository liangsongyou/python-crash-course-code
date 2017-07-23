my_foods = ['pizza','falafel','carrot cake']
# this doesn't work
#friend_foods = my_foods

# this does
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:\n{}".format(my_foods))
print("\nMy friend's favorite foods are:\n {}".format(friend_foods))

# using for loops to print the lists
print("\nMy favorite foods are:")
for food in my_foods:
    print("{}".format(food))

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print("{}".format(food))